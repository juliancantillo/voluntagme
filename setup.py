# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import my_project
version = my_project.__version__

setup(
    name='My Project Name',
    version=version,
    author='',
    author_email='support@inqbation.com',
    packages=[
        'my_project',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['my_project/manage.py'],
)