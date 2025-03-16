# 修改和增加类属性

# 1、从内部增加和修改类属性
class ClassA():
    # 定义类属性
    name = 'AnWen'
    
    @classmethod
    def fun1(cls):
        # 在类方法中增加类属性
        cls.age = 18
        # 打印类属性
        print(cls.name , cls.age)    
        
# 调用类方法，增加类属性
ClassA.fun1()

# 从外部修改类属性
ClassA.name = 'lucky'
ClassA.age = 20
# 再次调用类方法，打印修改后的类属性
ClassA.fun1()

# 2、从外部增加类属性
ClassA.gender = 'Male'
print(ClassA.gender)  # 打印新增的类属性

# 3、删除类属性
del ClassA.age
# 尝试访问已删除的类属性会报错
# print(ClassA.age)  # AttributeError: type object 'ClassA' has no attribute 'age'

# 4、访问类属性
print(ClassA.name)  # 访问类属性