# 类方法
class ClassA():
    var1 = 'AnWen'  # 类属性

    # 声明该方法是类方法, 只有声明了是类方法，才能使用类属性.
    # 类方法传参
    @classmethod
    def fun1(cls, age):
        print('fun1')
        print('我是：' + cls.var1)  # 访问类属性
        print('年龄：' + str(age))  # 打印传入的参数

    # 类方法可以用于修改类属性
    @classmethod
    def set_var1(cls, value):
        cls.var1 = value

# 调用类方法
ClassA.fun1(18)

# 修改类属性
ClassA.set_var1('NewValue')
ClassA.fun1(25)

# 类方法的更多解释：
# 1. 类方法使用 @classmethod 装饰器。
# 2. 类方法的第一个参数是 cls，表示类本身。
# 3. 类方法可以访问和修改类属性。
# 4. 类方法可以通过类名直接调用，也可以通过类的实例调用。

# 示例：通过实例调用类方法
instance = ClassA()
instance.fun1(30)
instance.set_var1('AnotherValue')
instance.fun1(35)


