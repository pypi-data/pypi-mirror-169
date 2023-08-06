#!/usr/bin/env python3

"""bashmocker - a hack for intercepting subprocess calls to test shell scripts in Python"""

import os
import subprocess
from tempfile import mkdtemp
from shutil import rmtree


class BashMocker:
    """A helper class that provides a way to replace tools with dummy
       calls and then summarize what was called.
       The idea is to make something vaguely similar to Test::Mock. I
       wouldn't say this is fully robust but for unit tests it does the job.

       Given a shell script named foo.sh:
         #!/bin/bash
         mycmd 1
         mycmd 2

       We can run the script with commands mocked out:
         with BashMocker('mycmd') as bm:
            bm.runscript('foo.sh')

            #Check that foo.sh called mycmd twice.
            assert len(bm.last_calls['mycmd']) == 2

       I made this for testing BASH scripts but in fact any program that calls
       other programs and respects env['PATH'] is testable this way.
    """

    def __init__(self, *mocks, shell=None):
        self.mock_bin_dir = mkdtemp()

        # The shell may be changed to /bin/sh or /bin/dash or but the normal default of
        # /bin/bash should be fine regardless of what you are testing.
        self._shell = shell or "/bin/bash"
        self._sh_env_val = None

        self._make_mockscript("_MOCK", 0)
        self._make_mockscript("_MOCKF", 1)
        self._make_mockscript("_MOCK_NOLOG", 0, log=False)
        self._make_mockscript("_MOCKF_NOLOG", 1, log=False)

        self.mocks = set()
        self.mocks_nolog = set()
        for m in mocks:
            self.add_mock(m)

        self.last_calls = None
        self.last_stderr = None
        self.last_stdout = None

    def _make_mockscript(self, mockname, retcode, log=True, side_effect="#NOP"):
        """Internal function for making mock scripts.
        """

        # To make the saving of args robust I had this idea:
        # for x in "$@" ; do _fs+=(%q) ; done
        # printf "%q %d ${_fs[*]}\n" "$0" "$#" "$@"
        # But using zeros seems better.
        # Also I want this to work in both BASH and DASH which is tricky.
        shell = self._shell
        if log:
            mockscript = r'''
             #!{shell}
             _fs=%s\\0%d\\0 ; for x in "$@" ; do _fs="$_fs"%s\\0 ; done ; _fs="$_fs"\\n
             printf "$_fs" "$(basename "$0")" "$#" "$@" >> "$(dirname "$0")"/_MOCKCALLS
             {side_effect}
             exit {retcode}
            '''
        else:
            mockscript = r'''
             #!{shell}
             {side_effect}
             exit {retcode}
            '''
        mockscript = mockscript.format(**locals())

        with open(os.path.join(self.mock_bin_dir, mockname), 'w') as fh:
            print(mockscript.strip(), file=fh)

            # copy R bits to X to achieve chmod +x
            mode = os.stat(fh.fileno()).st_mode
            os.chmod(fh.fileno(), mode | (mode & 0o444) >> 2)

    def _add_mockfunc(self, funcname, retcode, log=True, side_effect="#NOP"):
        """Internal function for writing mock functions.
           Note these will only apply to scripts that explicitly use #!/bin/bash
           as the interpreter, not #!/bin/sh or #!/bin/dash or anything
           called indirectly within the script, like 'env /bin/true ...'.
        """
        # This hack only works on BASH by setting BASH_ENV. DASH does not read any preable for
        # non-interactive scripts so there seems to be no easy way to poke one in.
        if not self._shell.endswith('/bash'):
            raise RuntimeError("Only BASH allows setting a preamble for scripts")

        if log:
            mockfunc = r'''
             {funcname}(){{
             local _fs
             _fs=%s\\0%d\\0 ; for x in "$@" ; do _fs="$_fs"%s\\0 ; done ; _fs="$_fs"\\n
             printf "$_fs" '{funcname}' "$#" "$@" >> "$(dirname "$BASH_SOURCE")"/_MOCKCALLS
             {side_effect}
             return {retcode} ; }}
            '''
        else:
            mockfunc = r'''
             {funcname}(){{
             {side_effect}
             return {retcode} ; }}
            '''
        mockfunc = mockfunc.format(**locals())

        with open(os.path.join(self.mock_bin_dir, '_BASH_ENV'), 'a') as fh:
            print(mockfunc.strip(), file=fh)

        self._sh_env_val = os.path.join(self.mock_bin_dir, "_BASH_ENV")

    def add_mock(self, mock, fail=False, log=True, side_effect=None):
        """Make a symlink named <mock> so the mock script will get called in
           place of the given command.
           Except if mock contains a / character - then bashmocker will try to use
           functions instead.

           If log is False then calls to this command will not be logged.

           If a side_effect is specified this shell code will be run as part of the
           script.
        """
        if '/' in mock:
            # We can still mock these by defining BASH functions.
            # TODO - should we do this for builtins too?
            self._add_mockfunc(mock, 1 if fail else 0, log=log, side_effect=side_effect)

        else:

            symlink = os.path.join(self.mock_bin_dir, mock)

            if side_effect:
                # We need a special script then
                target = "_MOCK_" + mock
                self._make_mockscript(target, 1 if fail else 0, log=log, side_effect=side_effect)
            else:
                if log:
                    target = "_MOCKF" if fail else "_MOCK"
                else:
                    target = "_MOCKF_NOLOG" if fail else "_MOCK_NOLOG"

            # If the link already exists, remove it
            try:
                os.unlink(symlink)
            except FileNotFoundError:
                pass

            os.symlink(target, symlink)

        if log:
            self.mocks.add(mock)
        else:
            self.mocks_nolog.add(mock)

    def cleanup(self):
        """Clean up
        """
        rmtree(self.mock_bin_dir)
        self.mock_bin_dir = None

    def runscript(self, cmd, set_path=True, env=None):
        """Runs the specified command, which may contain shell syntax if
           it is a string or else may be a list of literal [cmd, arg1, arg2, ...]
           and captures the output and the commands that were invoked.

           By default, the mock scripts will be prepended to the PATH, but you
           can alternatively specify set_path=False in which case you take
           responsibility for adding bm.mock_bin_dir to the PATH.

           If env is supplied, it must be a dict of strings. Items in env will
           be added to the execution environment.
        """
        # Cleanup _MOCKCALLS if found
        calls_file = os.path.join(self.mock_bin_dir, "_MOCKCALLS")
        try:
            os.unlink(calls_file)
        except FileNotFoundError:
            pass

        full_env = None
        if env:
            full_env = os.environ.copy()
            full_env.update(env)

        if set_path:
            full_env = full_env or os.environ.copy()
            if full_env.get('PATH'):
                full_env['PATH'] = os.path.abspath(self.mock_bin_dir) + ':' + full_env['PATH']
            else:
                full_env['PATH'] = os.path.abspath(self.mock_bin_dir)

            if self._sh_env_val:
                # Note - interactive scripts shouldn't normally depend on BASH_ENV,
                # so complain if I'm clobbering it. Ditto for ENV, but we don't need that
                # as BASH in compatibility mode won't set the functions we need.
                if full_env.get('BASH_ENV'):
                    raise RuntimeError("BASH_ENV was already set")

                # Rather than working out which is needed, set both.
                full_env['BASH_ENV'] = self._sh_env_val

        use_shell = (type(cmd) == str)
        p = subprocess.Popen(cmd,
                             shell = use_shell,
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE,
                             universal_newlines = True,
                             env = full_env,
                             executable = self._shell if use_shell else None,
                             close_fds = True)

        self.last_stdout, self.last_stderr = p.communicate()

        # Fish the MOCK calls out of _MOCKCALLS
        # Each line is \0 delimited but there may also be embedded newlines in
        # the arguments, so we read it in a funny way. I could just slurp the file
        # instead, I guess.
        calls = self.empty_calls()
        try:
            with open(calls_file, newline='\n') as fh:
                for aline in fh:
                    mock_name, mock_argc, mock_argv = aline.split('\0', 2)
                    while mock_argv.count('\0') < int(mock_argc):
                        # Must be an embedded newline; pull the next line
                        mock_argv += next(fh)
                    # The line should end in \0 so discard the last ''
                    mock_args = mock_argv.rstrip('\n').split('\0')[:-1]
                    calls[mock_name].append(mock_args)
        except FileNotFoundError:
            # So, nothing ran
            pass

        self.last_calls = calls

        # Return whatever the process returned
        return p.returncode

    def empty_calls(self):
        """Get the baseline dict of calls. Useful for tests to assert that
             bm.last_calls == bm.empty_calls()
           ie. nothing happened.
        """
        return { m : [] for m in self.mocks }

    # Allow the class to be used in a "with" construct, though
    # in a TestCase you probably want to use setup/teardown.
    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.cleanup()
