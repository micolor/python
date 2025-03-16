# 定义一个类 ClassA
class ClassA():
    # 类变量
    var1 = 100
    var2 = 0.01
    var3 = 'AnWen'
    
    # 构造函数
    def __init__(self, instance_var1, instance_var2):
        # 实例变量
        self.instance_var1 = instance_var1
        self.instance_var2 = instance_var2
    
    # 类方法
    def fun1():
        print('我是 fun1')

    def fun2():
        print('我是 fun2')

    def fun3():
        print('我是 fun3')
    
    # 实例方法
    def instance_fun(self):
        print(f'实例变量1: {self.instance_var1}, 实例变量2: {self.instance_var2}')

# 访问类变量
print(ClassA.var1)  
print(ClassA.var2)  
print(ClassA.var3)  

ClassA.fun1()  
ClassA.fun2()  
ClassA.fun3()  

# 创建类的实例
obj = ClassA('实例值1', '实例值2')

# 访问实例变量和实例方法
print(obj.instance_var1)
print(obj.instance_var2)
obj.instance_fun()