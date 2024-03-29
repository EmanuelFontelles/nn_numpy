# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='nn_numpy',
    version='0.0.1',
    description='A package which contains a simple implementation of neural network with numpy',
    long_description=readme,
    long_description_content_type='text/rst',
    author='Emanuel Fontelles',
    author_email='emanuelfontelles@hotmail.com',
    url='https://github.com/EmanuelFontelles/nn_numpy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

