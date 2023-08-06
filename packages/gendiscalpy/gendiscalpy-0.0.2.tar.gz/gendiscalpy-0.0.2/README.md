# gendiscalpy

Python bindings to [GenDisCal](https://github.com/LM-UGent/GenDisCal) and addition of phylogenetic tree function

- GenDisCal repo: https://github.com/LM-UGent/GenDisCal
- GenDisCal paper: https://academic.oup.com/bioinformatics/article/36/8/2337/5695704

## Installation

This package was created using `Python 3.9`.

```bash
pip install git+https://github.com/MrTomRod/gendiscalpy
```

This will add two scripts to your PATH:

- install_gendiscal
- gendiscal_tree

## Usage in terminal

### `install_gendiscal`

This script downloads the GenDisCal binary and unpacks it to a path of your choosing.

```text
$ install_gendiscal 
Options:
  1: /home/user/PycharmProjects/venvs/gendiscalpy10/bin
  2: /home/user/miniconda3/condabin
  3: /home/user/bin
  4: /usr/bin
  5: /usr/sbin
Please select a path to install GenDisCal to!
1
You chose: /home/user/PycharmProjects/venvs/gendiscalpy10/bin
Installed GenDiscal here: /home/user/PycharmProjects/venvs/gendiscalpy10/bin/GenDisCal
```

Now, you should be able to run GenDisCal in your terminal. Test with `GenDisCal --version`.

### `gendiscal_tree`

Create a phylogenetic tree based on GenDisCal a distance matrix. Returns
[Newick format](https://en.wikipedia.org/wiki/Newick_format).

This script uses the `upmga` algorithm of the `biotite` package. See
[wikipedia](https://en.wikipedia.org/wiki/UPGMA) and
[biotite docs](https://www.biotite-python.org/apidoc/biotite.sequence.phylo.upgma.html).

Requires GenDisCal to be in PATH, see also `install_gendiscal`.

Examples:

````shell
gendiscal_tree from_files assembly1.fna assembly2.fna
gendiscal_tree from_files assemblies/*.fna
gendiscal_tree from_files assemblies/*.fna --preset PaSiT6 --method euclidian
````

## Usage as Python class

```python
from gendiscalpy import GenDisCal, GenDisCalTree
from gendiscalpy.install_gendiscal import install

# install GenDisCal to /home/user/bin/GenDisCal
install(path='/home/user/bin')

gdc = GenDisCal()  # bin='/home/user/bin/GenDisCal'

# these commands return pandas.DataFrame objects
table1 = gdc.run('test-data/*.fna')
table2 = gdc.run('test-data/*.fna', preset='PaSiT6', method='euclidian')
distance_matrix = gdc.run('test-data/*.fna', distance_matrix=True)
histogram = gdc.run('test-data/*.fna', histogram=True)

# this command returns a float
val = gdc.compare_two(assembly_1='test-data/FAM3257-i1-1.fna', assembly_2='test-data/FAM13496-i1-1.fna')

# this command returns a string in Newick format
newick = GenDisCalTree.from_files('test-data/*.fna')
```
