# -*- coding: utf-8 -*-

"""
    pyasm
    ~~~~~

    :copyright: 2008 by Florian Boesch <pyalot@gmail.com>.
    :license: GNU AGPL v3 or later, see LICENSE for more details.
"""
    
from setuptools import setup
import os

setup(
    name                    = 'pyasm',
    version                 = '0.1.0', 
    description             = 'a pure python assembler',
    long_description        = __doc__,
    license                 = 'GNU AFFERO GENERAL PUBLIC LICENSE (AGPL) Version 3',
    url                     = 'http://hg.codeflow.org/pyasm',
    download_url            = 'http://hg.codeflow.org/',
    author                  = 'Florian Boesch',
    author_email            = 'pyalot@gmail.com',
    maintainer              = 'Florian Boesch',
    maintainer_email        = 'pyalot@gmail.com',
    zip_safe                = True,
    include_package_data    = True,
    packages                = ['pyasm', 'pyasm.instructions'],
    install_requires        = ['setuptools'],
    platforms               = ['any'],
    scripts                 = ['pyasm/pyasm'],
)
