from functools import cached_property

from . import __expected_gendiscal_version__
import logging
import os
import numpy as np
import pandas as pd
from io import StringIO
from subprocess import run, PIPE
from .utils import is_installed, check_output

PACKAGE_ROOT = os.path.dirname(__file__)


class GenDisCal:
    def __init__(self, bin: str = None):
        self.bin = 'GenDisCal' if bin is None else bin
        assert is_installed(self.bin), f'GenDisCal binary is missing! {self.bin=}'
        if not self.version == __expected_gendiscal_version__:
            logging.warning(
                f'GenDisCal version does not match GenDisCal.py! expected={__expected_gendiscal_version__}; real=')

    @cached_property
    def version(self) -> str:
        """
        Get version of GenDisCal binary

        :return: version (string)
        """
        command = [self.bin, '--version']
        subprocess = run(command, stdout=PIPE, stderr=PIPE, encoding='ascii')
        check_output(subprocess)
        return subprocess.stdout.strip()

    def compare_two(self, assembly_1: str, assembly_2: str, preset: str = None, method: str = None) -> np.float64:
        # Throw error if files are not readable (see https://github.com/LM-UGent/GenDisCal/issues/2)
        for file in (assembly_1, assembly_2):
            if not os.access(file, os.R_OK):
                raise IOError(f'Cannot read assembly={file}')

        stdout = self._run(assembly_1, assembly_2, preset=preset, method=method)
        table = self._parse_table(stdout=stdout)

        return table.Distance.max()

    def run(
            self,
            *files: [str],
            file_list: bool = False,
            distance_matrix: bool = False,
            histogram: bool = False,
            preset: str = None,
            method: str = None
    ) -> pd.DataFrame:
        """
        Execute GenDisCal, return table/distance-matrix/histogram as pd.DataFrame

        :param files: list of fasta files
        :param file_list: (optional) file containing a list of paths to files to use
        :param preset: use a special preset of options (more info: run 'GenDisCal --preset -h')
        :param method:  distance calculation method to be used (more info: run 'GenDisCal --method -h')
        :param distance_matrix: if true, return distance matrix instead of table
        :param histogram:  if true, return histogram instead of table
        :return: table/distance-matrix/histogram as pd.DataFrame
        """
        stdout = self._run(*files, file_list=file_list, distance_matrix=distance_matrix, histogram=histogram,
                           preset=preset, method=method)

        if distance_matrix:
            return self._parse_dist(stdout)
        elif histogram:
            return self._parse_hist(stdout)
        else:
            return self._parse_table(stdout)

    def _run(
            self,
            *files: [str],
            file_list: bool = False,
            distance_matrix: bool = False,
            histogram: bool = False,
            preset: str = None,
            method: str = None
    ) -> str:
        """
        Execute GenDisCal, return table/distance-matrix/histogram raw string (stdout)

        :param files: list of fasta files
        :param file_list: (optional) file containing a list of paths to files to use
        :param preset: use a special preset of options (more info: run 'GenDisCal --preset -h')
        :param method:  distance calculation method to be used (more info: run 'GenDisCal --method -h')
        :param distance_matrix: if true, return distance matrix instead of table
        :param histogram:  if true, return histogram instead of table
        :return: table/distance-matrix/histogram as pd.DataFrame
        """
        assert files, f'No files were specified! {files=}'
        assert not (
                    distance_matrix and histogram), f'Error: options distance_matrix and histogram are mutually exclusive!'

        command = [self.bin]

        if type(preset) is str:
            command.extend(['--preset', preset])
        if type(method) is str:
            command.extend(['--method', method])

        if file_list:
            command.append('--filelist')

        command += list(files)

        if distance_matrix:
            command.append('--distancematrix')
        elif histogram:
            command.append('--histogram')

        subprocess = run(' '.join(command), stdout=PIPE, stderr=PIPE, encoding='ascii', shell=True)
        check_output(subprocess)

        logging.info('command=' + ' '.join(command))

        return subprocess.stdout.strip()

    @staticmethod
    def _parse_table(stdout: str) -> pd.DataFrame:
        res = pd.read_csv(
            StringIO(stdout), sep=',',
            dtype={'File1': str, 'File2': str, 'Expected_Relation': str, 'Distance': np.float64}
        )
        columns = res.columns.tolist()
        assert columns == ['File1', 'File2', 'Expected_Relation', 'Distance'], f'Columns not as expected: {columns}'
        return res

    @staticmethod
    def _parse_hist(stdout: str) -> pd.DataFrame:
        res = pd.read_csv(
            StringIO(stdout), sep=',',
            dtype={'bin': np.float64, '?': np.float64},
            index_col='bin'
        )
        columns = res.columns.tolist()
        assert columns == ['?'], f'Columns not as expected: {columns}'
        return res

    @staticmethod
    def _parse_dist(stdout: str) -> pd.DataFrame:
        res = pd.read_csv(
            StringIO(stdout), sep=',',
            index_col=0
        )
        assert res.values.dtype == np.float64, f'Table must contain only floats: {res.values.dtype}'
        assert list(res.columns) == list(res.index), 'Table must be symmetrical!'
        assert np.allclose(res, res.T), 'Table must be symmetrical!'
        return res


def main():
    from fire import Fire

    gdc = GenDisCal()
    Fire(gdc._run)


if __name__ == '__main__':
    main()
