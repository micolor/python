# 元类示例
# 1. 类也是对象
class ObjectCreator(object):
    """这是一个简单的类"""
    pass
def echo(ob):
    print(ob)

mObject = ObjectCreator()
print(mObject)

# 可以直接打印一个类，因为它其实也是一个对象
print(ObjectCreator)
# 可以直接把一个类作为参数传给函数（注意这里是类，是没有实例化的）
echo(ObjectCreator)
# 也可以直接把类赋值给一个变量
objectCreator = ObjectCreator
print(objectCreator)