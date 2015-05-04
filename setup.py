#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='yeelink',
      version='1.1',
      keywords=('Yeelink', 'Yeelink API'),
      description='Yeelink SDK for python',
      long_description='See http://github.com/yeelink-python-sdk',
      license='MIT License',

      url='http://liluo.github.com/douban-client',
      author='smallmuou',
      author_email='lvyexuwenfa100@126.com',

      packages=find_packages(),
      include_package_data=True,
      platforms='any',
      install_requires=[],
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],)
