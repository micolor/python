# 动态创建类示例
# 类也是对象

# 动态创建类的函数
def create_class(name):
    if name == 'Foo':
        # 动态创建类 Foo
        class Foo:
            pass
        return Foo
    else:
        # 动态创建类 Bar
        class Bar:
            pass
        return Bar

# 使用 create_class 函数动态创建类
MyClass = create_class('Foo')
print(MyClass)  # 输出 <class '__main__.Foo'>
print(MyClass())  # 输出 <__main__.Foo object at 0x...>

# 定义一个简单的类 Hello
class Hello:
    def hello(self, name='Py'):
        print('Hello,', name)

# 类也是对象
# 类是 type 类的实例
print(type(Hello))  # 输出 <class 'type'>
print(type(MyClass))  # 输出 <class 'type'>

# 可以动态创建类的实例
hello_instance = Hello()
hello_instance.hello()  # 输出 Hello, Py