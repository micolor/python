# 基本数据类型转换

# 1. int(x [,base ]) 将x转换为一个整数
# 如果x是浮点数，则舍弃小数部分。如果x是字符串，则根据给定的进制base转换。
print(int(88.88))  # 88
print(int('100', 2))  # 4

# 2. float(x) 将x转换到一个浮点数
# 可以将整数和字符串转换为浮点数。
print(float(1))  # 1.0
print(float('3.14'))  # 3.14

# 3. complex(real [,imag ]) 创建一个复数
# real为实部，imag为虚部。如果省略imag，则默认为0。
print(complex(1, 2))  # (1+2j)
print(complex(3))  # (3+0j)

# 4. str(x) 将对象 x 转换为字符串
# 可以将任何对象转换为字符串。
print(str('Hello\nWorld'))  # Hello\nWorld
print(str(123))  # '123'

# 5. repr(x) 将对象 x 转换为表达式字符串
# 返回一个对象的字符串表示，可以用来重新创建该对象。
print(repr('Hello\nWorld'))  # 'Hello\nWorld'
print(repr(123))  # '123'

# 6. eval(str) 用来计算在字符串中的有效 Python 表达式,并返回一个对象
# 可以将字符串中的表达式求值并返回结果。
print(eval('1+2'))  # 3
print(eval('3.14 + 2'))  # 5.14

# 7. tuple(s) 将序列 s 转换为一个元组
# 可以将列表或字符串转换为元组。
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(tuple('abc'))  # ('a', 'b', 'c')

# 8. list(s) 将序列 s 转换为一个列表
# 可以将元组或字符串转换为列表。
print(list((1, 2, 3)))  # [1, 2, 3]
print(list('abc'))  # ['a', 'b', 'c']

# 9. chr(x) 将一个整数转换为一个字符
# x是0到255之间的整数，返回对应的字符。
print(chr(97))  # a
print(chr(65))  # A

# 10. ord(x) 将一个字符转换为它的整数值
# 返回字符对应的ASCII值。
print(ord('a'))  # 97
print(ord('A'))  # 65

# 11. hex(x) 将一个整数转换为一个十六进制字符串
# 返回整数x的十六进制表示。
print(hex(97))  # 0x61
print(hex(255))  # 0xff

# 12. oct(x) 将一个整数转换为一个八进制字符串
# 返回整数x的八进制表示。
print(oct(97))  # 0o141
print(oct(255))  # 0o377