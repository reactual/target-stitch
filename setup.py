#!/usr/bin/env python

from setuptools import setup

setup(name='target-stitch',
      version='1.6.3',
      description='Singer.io target for the Stitch API',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['target_stitch'],
      install_requires=[
          'jsonschema==2.6.0',
          'mock==2.0.0',
          'requests==2.18.4',
          'singer-python==3.5.1',
          'psutil==5.3.1'
      ],
      entry_points='''
          [console_scripts]
          target-stitch=target_stitch:main
      ''',
      packages=['target_stitch'],
)
