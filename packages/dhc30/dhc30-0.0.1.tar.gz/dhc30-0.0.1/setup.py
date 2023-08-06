import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1' 
PACKAGE_NAME = 'dhc30' 
AUTHOR = 'Duver Hernanez Cobos'

LICENSE = 'MIT'

INSTALL_REQUIRES = [
      'numpy'
      ]

setup(
    name='dhc30',
    version='0.0.1',
    author='Duver Hernandez Cobos',
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    include_package_data=True
)