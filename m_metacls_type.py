#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 动态创建类

# 函数和类的定义不是编译定义的，而是运行时动态创建的
class Hello(object):
    def hello(self, name='Py'):
        print('Hello,', name)
