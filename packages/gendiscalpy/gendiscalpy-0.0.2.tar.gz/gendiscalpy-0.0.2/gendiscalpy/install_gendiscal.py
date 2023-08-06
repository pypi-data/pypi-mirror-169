import os
from urllib import request
import tarfile
from . import __gendiscal_binary_url__
from .utils import query_options, get_paths


def download_and_extract(target_path: str) -> str:
    temp_file, headers = request.urlretrieve(
        url=__gendiscal_binary_url__
    )

    with tarfile.open(temp_file) as tar:
        tar.extract(member='GenDisCal', path=target_path)

    os.remove(temp_file)

    gendiscal_bin = f'{target_path}/GenDisCal'

    assert os.access(gendiscal_bin, os.X_OK), f'GenDisCal binary is not executable! {gendiscal_bin=}'

    return gendiscal_bin


def select_path() -> str:
    path = query_options(options=get_paths(), question='Please select a path to install GenDisCal to!')
    return path


def install(path: str = None):
    if path is None:
        path = select_path()
    assert os.path.isdir(path), f'Error: Directory does not exist: {path=}'

    gendiscal_bin = download_and_extract(target_path=path)

    print(f'Installed GenDiscal here: {gendiscal_bin}')


def main():
    from fire import Fire

    Fire(install)


if __name__ == '__main__':
    main()
