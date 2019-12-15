#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time         : 2018/10/20 21:41
# @email        : spirit_az@foxmail.com
# @fileName     : setup.py
__author__ = 'ChenLiang.Miao'


#--+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+--#
from distutils.core import setup
from Cython.Build import cythonize
setup(name = 'Hello world',
      ext_modules = cythonize("D:\\MCL\\python\\MCLPlayer\\source\\UI\\QSS.py"))
