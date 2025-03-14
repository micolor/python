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

# 调用类方法
ClassA.fun1(18)


