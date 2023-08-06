import os
from subprocess import CompletedProcess


def check_output(subprocess: CompletedProcess, exit_code: int = 0, min_stdout_len=1) -> None:
    if not subprocess.returncode == exit_code and len(subprocess.stdout) > min_stdout_len:
        raise AssertionError('\n'.join([
            f'Command failed: {subprocess.args}',
            f'Exit code: {subprocess.returncode}',
            f'Stdout: {subprocess.stdout}',
            f'Stderr: {subprocess.stderr}']))


def get_paths() -> [str]:
    return os.environ['PATH'].split(os.pathsep)


def is_installed(program):
    """
    Test if a program is installed.

    :param program: path to executable or command
    :return: if program executable: program; else None
    """

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:  # check if path to program is valid
        return is_exe(program)
    else:  # check if program is in PATH
        for path in get_paths():
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
        return False


def query_options(options: [str], question: str = 'Please select an option', error_msg='Please respond with a valid integer.') -> str:
    id_to_option = dict(enumerate(options, start=1))

    print('Options:')
    for id, path in id_to_option.items():
        print(f'  {id}: {path}')

    print(question)
    while True:
        choice = input()
        if choice.isdigit():
            choice = int(choice)
        if choice in id_to_option:
            result = id_to_option[choice]
            print(f'You chose: {result}')
            return result
        else:
            print(error_msg)
