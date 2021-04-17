# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in oil_management/__init__.py
from oil_management import __version__ as version

setup(
	name='oil_management',
	version=version,
	description='app to manage oil and give permit to the trucks',
	author='ayman nasser',
	author_email='aymenit2008@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
