#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from m_metacls_type import Hello

# 第一部分：演示普通类的类型检查
h = Hello()
h.hello()

# Hello 是 class 所以 type(Hello) 返回的是 type
print(type(Hello))
# h 是实例 所以 type(h) 返回的是 Hello
print(type(h))


# 第二部分：使用type动态创建类
"""
使用type动态创建类的语法说明：
type(class_name, base_classes, attributes_dict)
参数说明：
1. class_name: 要创建的类的名称
2. base_classes: 父类集合，使用元组格式，即使是单个父类也需要加逗号
3. attributes_dict: 类的属性和方法字典
"""

# 定义将要作为类方法的函数
def printHello(self, name='Py'):
    """打印问候语的示例方法"""
    print('Hello', name)

# 使用type动态创建Hello类
# 等同于：
# class Hello(object):
#     def hello(self, name='Py'):
#         print('Hello', name)
Hello = type('Hello', 
            (object,), 
            {'hello': printHello})  # 使用字典设置类的属性和方法

# 演示使用动态创建的类
h = Hello()  # 实例化
h.hello()    # 调用方法
print(type(Hello))
print(type(h))