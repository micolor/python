# Magic Method（魔术方法）
# 在 Python 中，所有以 "__" 双下划线包起来的方法，都统称为"魔术方法"。这些方法在特定情况下会被自动调用。

class Person:
    pass

if __name__ == '__main__':
    print(dir(Person))

# 构造(__new__) 和初始化(__init__)
# __new__(cls) 作用是返回一个实例对象
# __init__(self) 作用是对实例进行初始化
class User:
    def __new__(cls, *args, **kwargs):
        print('1. 调用 __new__ 创建实例')
        return super(User, cls).__new__(cls)
    
    def __init__(self, name, age):
        print('2. 调用 __init__ 初始化实例')
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"User(name='{self.name}', age={self.age})"

# 测试代码
if __name__ == '__main__':
    print("\n# User类测试")
    user = User('AnWen', 18)
    print(repr(user))  # 调用 __repr__

# 更多魔术方法示例
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

# 测试代码
if __name__ == '__main__':
    print("\n# Vector类测试")
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    print(v1 + v2)  # 调用 __add__
    print(v1 * 3)   # 调用 __mul__
    print(3 * v1)   # 调用 __rmul__