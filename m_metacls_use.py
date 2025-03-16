# 拦截类的创建
# 修改类
# 返回修改之后的类

# 元类示例：将类的属性名转换为大写
# 元类是用于创建类的类。它们可以拦截类的创建过程，并对类进行修改。

class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        # cls: 当前准备创建的类的元类
        # name: 类的名称
        # bases: 类继承的基类
        # dct: 类的属性字典
        
        # 将所有不以'__'开头的属性名转换为大写
        uppercase_attr = {name.upper(): value for name, value in dct.items() if not name.startswith('__')}
        
        # 调用父类的__new__方法创建类
        return super().__new__(cls, name, bases, uppercase_attr)

# 使用元类
class Foo(metaclass=UpperAttrMetaclass):
    bar = 'bip'

# 检查类属性名是否被转换为大写
print(hasattr(Foo, 'bar'))  # 输出: False
print(hasattr(Foo, 'BAR'))  # 输出: True

# 创建类的实例并访问属性
f = Foo()
print(f.BAR)  # 输出: 'bip'