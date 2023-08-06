import setuptools
from setuptools import Extension
from Cython.Build import cythonize

with open('README.md', 'r') as fstream:
    long_description = fstream.read()


setuptools.setup(
    name='colloptpy',
    version='0.1.1',
    author='Christoph Hoeppke',
    description='Collocation optimisation software written in Python.',
    long_description=long_description,
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'torch',
        'functorch',
        'pandas'
    ],
)

