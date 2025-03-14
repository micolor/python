# 类和对象

class ClassA():
    name = 'AnWen'

    def fun1(self):
        print('name：' + self.name)

a = ClassA()
a.fun1() 
print(a.name)  

b = ClassA()
# 对象属性赋值不会改变类属性
b.name = 'lucky'
b.fun1() 
print(ClassA.name)  
# 改变类属性
ClassA.name = 'rich'

print(a.name)  

# 对象方法和类方法
c = ClassA()
c.fun1() 
def fun2(self):
    print('姓名：' + self.name)
# 重写类方法fun1
ClassA.fun1 = fun2
c.fun1()  

# 重写对象方法会报错
# 报错：TypeError: fun2() missing 1 required positional argument: 'self'
c.fun1 = fun2
c.fun1()  