#! /usr/bin/python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'NBR-hugh',
    'url': 'URL to get it'
    'download_url': 'Where to download it',
    'author_email': 'nbr19940905@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'package': ['NAME'],
    'Scripts': [],
    'name': 'projectname'

}

setup(**config)
