#!/usr/bin/python

from setuptools import setup

setup(
    name='Assistant-Cli',
    version='0.0.2',
    py_modules=['assistant'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        assistant=assistant:cli
    '''
)
