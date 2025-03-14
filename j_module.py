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