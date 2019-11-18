#!/usr/bin/python

from setuptools import setup

setup(
    name='Assistant-Cli',
    version='0.4.0',
    py_modules=['assistant'],
    install_requires=[
        'Click',
        'python-slugify',
        'beautifulsoup4'
    ],
    entry_points='''
        [console_scripts]
        assistant=assistant:cli
    '''
)
