#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'jango',
    'version': '0.0.7',
    'description': 'Command line based personal assistant for linux based systems.',
    'long_description': open('README.md').read(),
    'author': 'Rahul Arora',
    'author_email': 'coderahul94@gmail.com',
    'license': 'MIT',
    'test_suite': 'tests',
    'url': 'https://github.com/rahulxxarora/Jango',
    'install_requires': [
        'BeautifulSoup4>=4.3.1', 'requests', 'pywapi', 'wikipedia==1.4.0', 'mewe==1.0.2'
    ],
    'packages': [
        'jango',
        'tests'
    ],
    'classifiers': [
        'Programming Language :: Python',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License'
    ],
}

setup(**config)
