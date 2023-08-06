from setuptools import setup, Extension

version = '0.1.4'

long_description = '''
It provides a simple interface for quick and convenient work with MariaDB.
'''

setup(
    name='sqlib',

    version=version,

    packages=['sqlib'],
    install_requires=['mariadb'],

    url='https://github.com/meyiapir/sqlib',

    license='Apache License, Version 2.0, see LICENSE file',

    author='meyap',

    author_email='mmeyiapir@gmail.com',

    description='Sqlib is a small ORM for MariaDB.',

    description_content_type='text/markdown',

    long_description=open('README.md').read,
    long_description_content_type='text/markdown',
)
