# /usr/bin/python3
# -*- coding : utf-8 -*-
# @Author : zhao jun
# @Email : 公共开发技术
# @File : setup.py.py

from distutils.core import setup
from setuptools import find_packages
with open("C:/users/www/desktop/Pypi_shili/README.rst") as filename :
    content = filename.read()

setup(name="package_zhao",  # 包名
      version="3.0.0",  # 版本号
      description="A small example package",
      long_description=content,
      author="jun zhao e",
      author_email="1144657335@qq.com",
      url="https://zhaojun.com",
      install_requires=[],
      license="MIT license",
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
                  'Intended Audience :: Developers',
                  'Operating System :: OS Independent',
                  'Natural Language :: Chinese (Simplified)',
                  'Programming Language :: Python',
                  'Programming Language :: Python :: 2',
                  'Programming Language :: Python :: 2.5',
                  'Programming Language :: Python :: 2.6',
                  'Programming Language :: Python :: 2.7',
                  'Programming Language :: Python :: 3',
                  'Programming Language :: Python :: 3.5',
                  'Programming Language :: Python :: 3.6',
                  'Programming Language :: Python :: 3.7',
                  'Programming Language :: Python :: 3.8',
                  'Topic :: Software Development :: Libraries'
              ],
      )