#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 动态创建类示例

# 导入模块
from m_metacls_obj import Hello

# 第一部分：演示普通类的类型检查
h = Hello()
h.hello()

print(type(Hello))  # 输出：<class 'type'>
print(type(h))  # 输出：<class '__main__.Hello'>

# 第二部分：使用 type 动态创建类
def printHello(self, name='Py'):
    print('Hello', name)

# 使用 type 动态创建 Hello 类
# type(name, bases, dict) -> a new type
# name: 类名
# bases: 基类的元组
# dict: 包含类属性和方法的字典
Hello = type('Hello', (object,), {'hello': printHello})

# 演示使用动态创建的类
h = Hello()
h.hello()
print(type(Hello))  # 输出：<class 'type'>
print(type(h))  # 输出：<class '__main__.Hello'>

# 第三部分：更复杂的动态创建类示例
def init(self, name):
    self.name = name

def repr(self):
    return f'Hello({self.name})'

# 动态创建带有 __init__ 和 __repr__ 方法的类
Hello = type('Hello', (object,), {'__init__': init, '__repr__': repr, 'hello': printHello})

# 演示使用新的动态创建的类
h = Hello('Python')
h.hello()
print(h)  # 输出：Hello(Python)
print(type(Hello))  # 输出：<class 'type'>
print(type(h))  # 输出：<class '__main__.Hello'>