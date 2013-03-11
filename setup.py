#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django_hospital',
    version='1.0',
    description="",
    author="Lincoln Loop",
    author_email='info@lincolnloop.com',
    url='',
    packages=find_packages(),
    package_data={'django_hospital': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
