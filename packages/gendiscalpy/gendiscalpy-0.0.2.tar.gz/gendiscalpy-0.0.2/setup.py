# based on https://realpython.com/pypi-publish-python-package
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / 'README.md').read_text()

# This call to setup() does all the work
setup(
    name='gendiscalpy',
    version='0.0.2',
    description='Python bindings to GenDisCal and addition of phylogenetic tree function',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/MrTomRod/gendiscalpy',
    author='Thomas Roder',
    author_email='roder.thomas@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    packages=['gendiscalpy'],
    install_requires=['fire', 'pandas', 'biotite'],
    entry_points={
        'console_scripts': [
            'install_gendiscal=gendiscalpy.install_gendiscal:main',
            'gendiscal_tree=gendiscalpy.GenDisCalTree:main',
        ]
    },
)
