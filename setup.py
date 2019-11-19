#!/usr/bin/python

from setuptools import setup

setup(
    name='assistant-cli',
    version='0.4.0',
    author='Aaron Uurman',
    url='https://github.com/aaronuurman/assistant',
    description='This is a list of processes I have automated to make my life easier',
    py_modules=['assistant'],
    install_requires=[
        'Click',
        'python-slugify',
        'beautifulsoup4'
    ],
    entry_points='''
        [console_scripts]
        assistant=assistant.app:cli
    '''
)