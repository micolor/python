# 描述器

# 描述器是一个实现了描述器协议（__get__, __set__, __delete__ 方法）的类，用于控制另一个类的属性访问。
# 描述器可以用于实现属性的类型检查、计算属性、懒加载等功能。

# 描述器协议包含以下三个方法：
# 1.__get__(self, instance, owner)：
# 获取属性值时调用。
# 例如：obj.attr 会调用 attr.__get__(obj, type(obj))。
# 2.__set__(self, instance, value)：
# 设置属性值时调用。
# 例如：obj.attr = value 会调用 attr.__set__(obj, value)。
# 3.__delete__(self, instance)：
# 删除属性时调用。
# 例如：del obj.attr 会调用 attr.__delete__(obj)。

# 描述器分为两种类型：
# 1. 数据描述器：同时实现了 __get__ 和 __set__ 方法的描述器。
# 2. 非数据描述器：只实现了 __get__ 方法的描述器。

# 示例1: 基本的描述器
class NameDescriptor(object):
    def __init__(self, name='AnWen'):
        self.name = name

    def __get__(self, instance, owner):
        print('获取 name 值')
        return self.name

    def __set__(self, instance, value):
        print('设置 name 值')
        self.name = value

    def __delete__(self, instance):
        print('删除 name 值')
        del self.name

class User(object):
    name = NameDescriptor()

user = User()
print(user.name)  # 调用 __get__
user.name = 'Bob'  # 调用 __set__
print(user.name)  # 调用 __get__
del user.name  # 调用 __delete__

# 示例2: 单位转换描述器
class Meter(object):
    """米单位描述器"""
    def __init__(self, value=0.0):
        self.value = value
    
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, value):
        self.value = float(value)

class Foot(object):
    """英尺单位描述器(1米=3.2808英尺)"""
    def __get__(self, instance, owner):
        return instance.meter * 3.2808
    
    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808

class Distance(object):
    """使用描述器实现单位转换"""
    meter = Meter()  # 米
    foot = Foot()    # 英尺

if __name__ == '__main__':
    """演示单位转换描述器"""
    print("\n=== 单位转换描述器演示 ===")
    d = Distance()
    print("1. 初始值(米,英尺):", d.meter, d.foot)
    d.meter = 1
    print("2. 设置1米后(米,英尺):", d.meter, d.foot)
    d.foot = 3.2808
    print("3. 设置3.2808英尺后(米,英尺):", d.meter, d.foot)