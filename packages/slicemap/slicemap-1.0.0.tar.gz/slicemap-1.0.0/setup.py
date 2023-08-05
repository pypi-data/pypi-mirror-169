from setuptools import setup, find_packages

setup(
    name='slicemap',
    version='1.0.0',
    url='https://github.com/gahaalt/slicemap.git',
    author='Szymon Mikler',
    author_email='sjmikler@gmail.com',
    description='A tiny package containing a dict-like data structure with numeric'
                ' slices as keys.',
    packages=find_packages(),
    install_requires=['sortedcontainers>=2.4.0'],
)
