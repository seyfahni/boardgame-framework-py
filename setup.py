# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_agreement = f.read()

setup(
    name='boardgame-framework',
    version='1.0.0',
    description='simple library for creating boardgame logic',
    long_description=readme,
    author='Niklas Seyfarth',
    author_email='niklas@seyfarth.de',
    url='https://gitlab.com/seyfahni/boardgame-framework',
    license=license_agreement,
    packages=find_packages(exclude=('tests', 'docs'))
)
