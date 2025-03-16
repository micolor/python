# 类的访问控制
# 单下划线和双下划线的含义
# 单下划线（_）：表示受保护的变量，提示该变量仅供类内部和子类访问，但不会强制限制。
# 双下划线（__）：表示私有变量，触发名称改写机制，使得变量名变为 _ClassName__VariableName，从而避免子类覆盖。

# 在 Java 中：
# public：公共的，任何地方都可以访问。
# protected：受保护的，同一个包中的类和子类可以访问。
# private：私有的，只有类内部可以访问。

class UserInfo(object):
    def __init__(self, name, sex, age):
        self.name = name
        self._sex = sex
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
    

if __name__ == '__main__':
    user = UserInfo('AnWen', '男', 18)
    # 打印所有属性
    print(dir(user))
    # 打印构造函数中的属性
    print(user.__dict__)
    print(user.get_age())
    print(user._UserInfo__age)
    user.set_age(20)
    print(user.get_age())

# 类专有的方法
# __init__ 构造函数，在生成对象时调用
# __del__ 析构函数，释放对象时使用
# __repr__ 打印，转换
# __str__ 返回一个对象的字符串表示
# __setitem__ 按照索引赋值
# __getitem__ 按照索引获取值
# __len__ 获得长度
# __cmp__ 比较运算
# __call__ 函数调用
# __add__ 加运算
# __sub__ 减运算
# __mul__ 乘运算
# __truediv__ 真除运算
# __floordiv__ 地板除运算
# __mod__ 求余运算
# __pow__ 乘方

# 获取类的相关信息
# type(obj)：获取对象的类型
# isinstance(obj, type)：判断对象是否为指定类型的实例
# hasattr(obj, attr)：判断对象是否具有指定属性/方法
# getattr(obj, attr[, default])：获取属性/方法的值，没有则返回 default 值
# setattr(obj, attr, value)：设定属性/方法的值
# delattr(obj, attr)：删除属性
# dir(obj)：获取对象的所有属性和方法名的列表

# 方法的访问控制
class User(object):
    def public_method(self):
        pass

    def _protected_method(self):
        pass

    def __private_method(self):
        pass

    def access_methods(self):
        self.public_method()
        self._protected_method()
        self.__private_method()

if __name__ == '__main__':
    user = User()
    user.public_method()
    user._protected_method()
    # user.__private_method()  # 这行会报错，因为 __private_method 是私有方法
    user.access_methods()

