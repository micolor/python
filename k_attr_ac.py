# 属性的访问控制
# Python 提供了几种特殊方法来控制对象属性的访问：
# 1.__getattr__(self, name)：
# 当访问的属性不存在时调用。
# 例如：obj.non_existent_attr 会调用 obj.__getattr__('non_existent_attr')。
# 2.__setattr__(self, name, value)：
# 设置属性值时调用。
# 例如：obj.attr = value 会调用 obj.__setattr__('attr', value)。
# 3.__delattr__(self, name)：
# 删除属性时调用。
# 例如：del obj.attr 会调用 obj.__delattr__('attr')。
# 4.__getattribute__(self, name)：
# 访问任何属性时调用。
# 例如：obj.attr 会调用 obj.__getattribute__('attr')。
# 注意：__getattribute__ 会在每次访问属性时调用，即使属性存在。
# 5. __dir__(self)：
# 返回对象的属性列表。
# 例如：dir(obj) 会调用 obj.__dir__()。

class User(object):
    def __getattr__(self, name):
        print(f'[getattr] 尝试访问不存在的属性: {name}')
        return None

    def __setattr__(self, name, value):
        print(f'[setattr] 设置属性: {name} = {value}')
        super(User, self).__setattr__(name, value)

    def __delattr__(self, name):
        print(f'[delattr] 删除属性: {name}')
        super(User, self).__delattr__(name)

    def __getattribute__(self, name):
        print(f'[getattribute] 访问属性: {name}')
        return super(User, self).__getattribute__(name)

    def __dir__(self):
        print('[dir] 获取属性列表')
        return super(User, self).__dir__()

user = User()
user.name = 'Alice'  # 调用 __setattr__
print(user.name)     # 调用 __getattribute__
print(user.age)      # 调用 __getattr__
del user.name        # 调用 __delattr__
print(dir(user))     # 调用 __dir__