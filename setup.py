#!/usr/bin/python

from setuptools import setup

setup(
    name='Assistant-Cli',
    version='0.0.3',
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
