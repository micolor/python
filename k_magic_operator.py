# 运算符相关的魔术方法

# 比较运算符
# __eq__(self, other)	定义了比较操作符 == 的行为
# __ne__(self, other)	定义了比较操作符 != 的行为
# __lt__(self, other)	定义了比较操作符 < 的行为
# __gt__(self, other)	定义了比较操作符 > 的行为
# __le__(self, other)	定义了比较操作符 <= 的行为
# __ge__(self, other)	定义了比较操作符 >= 的行为

class Number(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        print('__eq__')
        return self.value == other.value

    def __ne__(self, other):
        print('__ne__')
        return self.value != other.value

    def __lt__(self, other):
        print('__lt__')
        return self.value < other.value

    def __gt__(self, other):
        print('__gt__')
        return self.value > other.value

    def __le__(self, other):
        print('__le__')
        return self.value <= other.value

    def __ge__(self, other):
        print('__ge__')
        return self.value >= other.value

if __name__ == '__main__':
    num1 = Number(2)
    num2 = Number(3)
    print('比较运算符演示:')
    print('num1 == num2 ? ----> {} \n'.format(num1 == num2))
    print('num1 != num2 ? ----> {} \n'.format(num1 != num2))
    print('num1 < num2 ? ----> {} \n'.format(num1 < num2))
    print('num1 > num2 ? ----> {} \n'.format(num1 > num2))
    print('num1 <= num2 ? ----> {} \n'.format(num1 <= num2))
    print('num1 >= num2 ? ----> {} \n'.format(num1 >= num2))


# 算数运算符
# __add__(self, other)	实现了加号运算
# __sub__(self, other)	实现了减号运算
# __mul__(self, other)	实现了乘法运算
# __floordiv__(self, other)	实现了 // 运算符
# __div__(self, other)	实现了/运算符. 该方法在 Python3 中废弃. 原因是 Python3 中，division 默认就是 true division
# __truediv__(self, other)	实现了 true division. 只有你声明了 from __future__ import division 该方法才会生效
# __mod__(self, other)	实现了 % 运算符, 取余运算
# __divmod__(self, other)	实现了 divmod() 內建函数
# __pow__(self, other)	实现了 ** 操作. N 次方操作
# __lshift__(self, other)	实现了位操作 <<
# __rshift__(self, other)	实现了位操作 >>
# __and__(self, other)	实现了位操作 &
# __or__(self, other)	实现了位操作 |
# __xor__(self, other)	实现了位操作 ^

class Calculator(object):
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        print('__add__')
        return Calculator(self.value + other.value)
        
    def __sub__(self, other):
        print('__sub__')
        return Calculator(self.value - other.value)
        
    def __mul__(self, other):
        print('__mul__')
        return Calculator(self.value * other.value)
        
    def __truediv__(self, other):
        print('__truediv__')
        return Calculator(self.value / other.value)

    def __floordiv__(self, other):
        print('__floordiv__')
        return Calculator(self.value // other.value)
        
    def __mod__(self, other):
        print('__mod__')
        return Calculator(self.value % other.value)
        
    def __pow__(self, other):
        print('__pow__')
        return Calculator(self.value ** other.value)
        
    def __lshift__(self, other):
        print('__lshift__')
        return Calculator(self.value << other.value)
        
    def __rshift__(self, other):
        print('__rshift__')
        return Calculator(self.value >> other.value)
        
    def __and__(self, other):
        print('__and__')
        return Calculator(self.value & other.value)
        
    def __or__(self, other):
        print('__or__')
        return Calculator(self.value | other.value)
        
    def __xor__(self, other):
        print('__xor__')
        return Calculator(self.value ^ other.value)

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    print('算术运算符演示:')
    calc1 = Calculator(10)
    calc2 = Calculator(5)
    print('10 + 5 = ', calc1 + calc2)
    print('10 - 5 = ', calc1 - calc2)
    print('10 * 5 = ', calc1 * calc2)
    print('10 / 5 = ', calc1 / calc2)
    print('10 // 5 = ', calc1 // calc2)
    print('10 % 5 = ', calc1 % calc2)
    print('10 ** 5 = ', calc1 ** calc2)
    print('10 << 5 = ', calc1 << calc2)
    print('10 >> 5 = ', calc1 >> calc2)
    print('10 & 5 = ', calc1 & calc2)
    print('10 | 5 = ', calc1 | calc2)
    print('10 ^ 5 = ', calc1 ^ calc2)