# 元类示例：查看类和实例的类型

# 元类是创建类的类。类是创建对象的模板，而元类是创建类的模板。
# 在Python中，所有的类都是由type这个元类创建的。

# 整型
age = 23
print(age.__class__)  # 输出：<class 'int'>

# 字符串
name = '两点水'
print(name.__class__)  # 输出：<class 'str'>

# 函数
def fu():
    pass

print(fu.__class__)  # 输出：<class 'function'>

# 实例
class Eat:
    pass

mEat = Eat()
print(mEat.__class__)  # 输出：<class '__main__.Eat'>

# 查看类的类，即元类
print(type(age))  # 输出：<class 'int'>
print(type(name))  # 输出：<class 'str'>
print(type(fu))  # 输出：<class 'function'>
print(type(mEat))  # 输出：<class '__main__.Eat'>
print(type(int))  # 输出：<class 'type'>
print(type(str))  # 输出：<class 'type'>
print(type(type))  # 输出：<class 'type'>

# 自定义元类
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f'Creating class {name}')
        return super().__new__(cls, name, bases, dct)

# 使用自定义元类
class MyClass(metaclass=MyMeta):
    pass

# 创建MyClass的实例
my_instance = MyClass()  # 输出：Creating class MyClass

# 查看MyClass的元类
print(type(MyClass))  # 输出：<class '__main__.MyMeta'>