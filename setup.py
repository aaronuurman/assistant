from setuptools import setup

setup(
    name='Assistant-Cli',
    version='0.0.1',
    py_modules=['assistant'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        assistant=assistant:cli
    '''
)