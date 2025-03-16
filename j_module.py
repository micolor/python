# 模块的使用
# 导入模块使用import关键字

# import整个模块
import math
_author_ = 'AnWen'
print(math.pi)  # 输出math模块中的pi常量

# import整个模块
import sys
print(sys.path)  # 输出sys模块中的path变量

# from ... import ... 语法： from 模块名 import 函数名，变量名，类名
from sys import path
print(path)  # 输出sys模块中的path变量

# from ... import * 导入模块中的所有内容
from sys import *
print(version)  # 输出sys模块中的version变量
print(executable)  # 输出sys模块中的executable变量

# 使用别名导入模块
import math as m
print(m.e)  # 输出math模块中的e常量

# 使用别名导入模块中的函数、变量、类
from math import pi as PI
print(PI)  # 输出math模块中的pi常量

# 自定义模块导入
# 假设有一个自定义模块 my_module.py，包含以下内容：
# def greet(name):
#     return f"Hello, {name}!"
# 导入并使用自定义模块
# import my_module
# print(my_module.greet("World"))

# 也可以使用 from ... import ... 语法导入自定义模块中的特定函数
# from my_module import greet
# print(greet("World"))

# 总结：
# 1. 使用 import 模块名 导入整个模块
# 2. 使用 from 模块名 import 函数名, 变量名, 类名 导入模块中的特定内容
# 3. 使用 from 模块名 import * 导入模块中的所有内容（不推荐，可能导致命名冲突）
# 4. 使用 as 关键字为模块或模块中的内容指定别名
# 5. 可以导入自定义模块，方法与导入标准库模块相同