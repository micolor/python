# 基本数据类型转换

# 1. int(x [,base ]) 将x转换为一个整数
print(int(88.88))  # 88
# 2. float(x) 将x转换到一个浮点数
print(float(1))  # 1.0
# 3. complex(real [,imag ]) 创建一个复数
print(complex(1, 2))  # (1+2j)
# 4. str(x) 将对象 x 转换为字符串
print(str('Hello\nWorld'))
# 5. repr(x) 将对象 x 转换为表达式字符串
print(repr('Hello\nWorld'))
# 6. eval(str) 用来计算在字符串中的有效 Python 表达式,并返回一个对象
print(eval('1+2'))  # 3
# 7. tuple(s) 将序列 s 转换为一个元组
print(tuple([1, 2, 3]))  # (1, 2, 3)
# 8. list(s) 将序列 s 转换为一个列表
print(list((1, 2, 3)))  # [1, 2, 3]
# 9. chr(x) 将一个整数转换为一个字符
print(chr(97))  # a
# 10. ord(x) 将一个字符转换为它的整数值
print(ord('a'))  # 97
# 11. hex(x) 将一个整数转换为一个十六进制字符串
print(hex(97))  # 0x61
# 12. oct(x) 将一个整数转换为一个八进制字符串
print(oct(97))  # 0o141

# 例子
str1 = '100'
str2 = '200'
print(str1 + str2)  # 100200
print(int(str1) + int(str2))  # 300
print(int(88.88))  # 88