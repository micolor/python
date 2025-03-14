# 定义一个类 ClassA
class ClassA():
    # 类变量
    var1 = 100
    var2 = 0.01
    var3 = 'AnWen'
    # 类方法
    def fun1():
        print('我是 fun1')

    def fun2():
        print('我是 fun2')

    def fun3():
        print('我是 fun3')

# 访问类变量
print(ClassA.var1)  
print(ClassA.var2)  
print(ClassA.var3)  

ClassA.fun1()  
ClassA.fun2()  
ClassA.fun3()  