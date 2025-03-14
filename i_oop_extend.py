# 类的继承
# class ClassName(Base1,Base2,Base3):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>
# 若是父类中有相同的方法名，而在子类使用时未指定, 会按从左到右的顺序查找 Base1 -> Base2 - > Base3

# 调用父类的方法
class UserInfo():
    lv = 5
    def __init__(self, name, age):
        self.name = name
        self._age = age
    @classmethod
    def get_lv(cls):
        return cls.lv

class UserInfo2(UserInfo):
    def __init__(self, name, age, sex):
        super(UserInfo2, self).__init__(name, age)
        self.sex = sex

if __name__ == '__main__':
    userInfo2 = UserInfo2('anwen', 23, '男')
    # 打印所有属性
    print(dir(userInfo2))
    # 打印构造函数中的属性
    print(userInfo2.__dict__)
    print(UserInfo2.get_lv())

# 子类的类型判断 isinstance
class Animal(object):
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(isinstance(dog, Cat))
    
    # 基本类型也可以用isinstance()判断
    print(isinstance('anwen', str))
    print(isinstance(123, int))
    print(isinstance(123, str))