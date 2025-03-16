# 类和对象

class ClassA():
    name = 'AnWen'

    def fun1(self):
        print('name：' + self.name)

# 创建对象a
a = ClassA()
a.fun1()  # 输出：name：AnWen
print(a.name)  # 输出：AnWen

# 创建对象b
b = ClassA()
# 对象属性赋值不会改变类属性
b.name = 'lucky'
b.fun1()  # 输出：name：lucky
print(ClassA.name)  # 输出：AnWen
# 改变类属性
ClassA.name = 'rich'

print(a.name)  # 输出：AnWen

# 对象方法和类方法
c = ClassA()
c.fun1()  # 输出：name：rich

def fun2(self):
    print('姓名：' + self.name)

# 重写类方法fun1
ClassA.fun1 = fun2
c.fun1()  # 输出：姓名：rich

# 重写对象方法会报错
# 报错：TypeError: fun2() missing 1 required positional argument: 'self'
c.fun1 = fun2
try:
    c.fun1()  # 这里会报错
except TypeError as e:
    print(e)  # 输出错误信息

# 新增知识点：类方法和静态方法
class ClassB:
    name = 'ClassB'

    @classmethod
    def class_method(cls):
        print('类方法：' + cls.name)

    @staticmethod
    def static_method():
        print('静态方法')

# 调用类方法
ClassB.class_method()  # 输出：类方法：ClassB

# 调用静态方法
ClassB.static_method()  # 输出：静态方法

# 创建对象d
d = ClassB()
d.class_method()  # 输出：类方法：ClassB
d.static_method()  # 输出：静态方法