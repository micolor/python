# 主模块和非主模块
# 在 Python 中，每个模块都有一个内置属性 __name__。
# 如果模块是被直接运行的，那么 __name__ 的值为 '__main__'。
# 如果模块是被导入的，那么 __name__ 的值为模块的名字。

if __name__ == '__main__':
    print('主模块')
else:
    print('非主模块')