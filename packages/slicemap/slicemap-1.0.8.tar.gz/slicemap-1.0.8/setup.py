from setuptools import setup, find_packages

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "slicemap" / "README.md").read_text()

setup(
    name='slicemap',
    version='1.0.8',
    url='https://github.com/gahaalt/slicemap.git',
    author='Szymon Mikler',
    license="MIT License",
    author_email='sjmikler@gmail.com',
    description='A tiny package containing a dict-like data structure with numeric'
                ' slices as keys.',
    packages=find_packages(),
    install_requires=['sortedcontainers>=2.4.0'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
