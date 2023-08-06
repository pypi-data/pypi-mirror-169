from .GenDisCal import GenDisCal
from biotite.sequence.phylo import upgma


class GenDisCalTree:
    @staticmethod
    def from_csv(csv: str) -> str:
        """
        Create a phylogenetic tree based on GenDisCal a distance matrix.

        :param csv: Path to distance matrix
        :return: Newick string
        """
        with open(csv) as f:
            distance_matrix = GenDisCal._parse_dist(f.read())
        tree = upgma(distance_matrix.values)
        newick = tree.to_newick(labels=distance_matrix.index)
        return newick

    @staticmethod
    def from_files(*files: [str], file_list: bool = False, preset: str = None, method: str = None) -> str:
        """
        Create a phylogenetic tree directly based on assembly FASTA files.

        :param files: list of fasta files
        :param file_list: (optional) file containing a list of paths to files to use
        :param preset: use a special preset of options (more info: run 'GenDisCal --preset -h')
        :param method:  distance calculation method to be used (more info: run 'GenDisCal --method -h')
        :return: Newick string
        """
        distance_matrix = GenDisCal().run(*files, distance_matrix=True, file_list=file_list, preset=preset, method=method)
        tree = upgma(distance_matrix.values)
        newick = tree.to_newick(labels=distance_matrix.index)
        return newick


def main():
    from fire import Fire

    Fire({
        'from_csv': GenDisCalTree.from_csv,
        'from_files': GenDisCalTree.from_files
    })


if __name__ == '__main__':
    main()
