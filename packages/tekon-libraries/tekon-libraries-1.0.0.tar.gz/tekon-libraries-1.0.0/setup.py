""" 

#################################################################################################
File used to create a Package.
* Dependencies for create Python Package: wheel, twine
* Prerequesites: test.pypi.org user with permission to edit library project
* Steps to create a package:
    - Open a terminal window on library directory
    - Execute the commands: 
        $python setup.py bdist_wheel
        $pip install -e .
        $python setup.py sdist
        $py -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
* To install package on any other device:
    - pip install -i https://test.pypi.org/simple/ tekonlibraries

#################################################################################################

Add a description on this Header for all Module files updates and change the version string below.

* 2022-09-14: v0.0.1
    - First version for testing package creation.
* 2022-09-14: v0.0.2
    - First Release on Development.
* 2022-09-22: v0.0.3
    - Add sst25vf memory library.	
"""
from setuptools import setup

setup(
    name='tekon-libraries',
    version='1.0.0',
    description='Tekon Python Libraries.',
    py_modules=["tekon_zeromq", "rcxxxx_tm_lib", "tekwi", "sst25vf"],
    package_dir={'': 'src'},
)