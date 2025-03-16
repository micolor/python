# 构造函数
# 创建实例时会自动被调用
# 构造函数用于初始化对象的属性

class ClassA():
    def __init__(self):
        print('init')

a = ClassA()

# 构造函数参数传递
# 构造函数可以接受参数，用于初始化对象的属性
class ClassB():
    def __init__(self, name):
        self.name = name
        print('init')

b = ClassB('AnWen')
print(b.name)

# 析构函数
# 析构函数在对象被删除时自动调用
# 析构函数用于执行清理工作，例如关闭文件或网络连接
class ClassC():
    def __init__(self):
        print('init')

    def __del__(self):
        print('del')

c = ClassC()

# 示例：带有参数的构造函数和析构函数
class ClassD():
    def __init__(self, name):
        self.name = name
        print(f'{self.name} init')

    def __del__(self):
        print(f'{self.name} del')

d = ClassD('Example')
print(d.name)

# 注意：在某些情况下，析构函数可能不会被立即调用，例如程序结束时
# 因此，不应依赖析构函数来执行关键的清理工作