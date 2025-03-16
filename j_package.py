# 包 Package

# 包是一个包含模块的目录，通常有一个 __init__.py 文件。
# 它帮助组织和管理代码，使其更易维护和重用。

# 示例结构：
# my_package/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# __init__.py 文件可以是空的，也可以包含包的初始化代码。
# 它的存在告诉 Python 这个目录应该被视为一个包。

# 导入包中的模块
# import my_package.module1
# from my_package import module2

# 也可以使用相对导入在包内导入模块
# from . import module1
# from .module2 import some_function

# 示例代码：
# my_package/module1.py
# def func1():
#     print("This is function 1 from module 1")

# my_package/module2.py
# def func2():
#     print("This is function 2 from module 2")

# my_package/__init__.py
# from .module1 import func1
# from .module2 import func2

# 使用包中的模块和函数
# import my_package
# my_package.func1()
# my_package.func2()

# 这样做的好处是可以将相关的模块组织在一起，避免命名冲突，并且可以更方便地管理和重用代码。