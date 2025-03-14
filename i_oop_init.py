# 构造函数
# 创建实例时会自动被调用

class ClassA():
    def __init__(self):
        print('init')


a = ClassA()

# 构造函数参数传递
# def __init__(self,[...):
class ClassB():
    def __init__(self, name):
        self.name = name
        print('init')


b = ClassB('AnWen')
print(b.name)


# 析构函数
# def __del__(self,[...):
class ClassC():
    def __init__(self):
        print('init')

    def __del__(self):
        print('del')
c = ClassC()