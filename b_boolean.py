# 布尔值
print(1 == 1)  # True，因为1等于1
print(1 == 2)  # False，因为1不等于2

# 布尔运算符
print(True and False)  # False，因为and运算符要求两个操作数都为True
print(True or False)   # True，因为or运算符只要求一个操作数为True
print(not True)        # False，因为not运算符取反

# 布尔值与其他数据类型
print(bool(0))         # False，0被认为是False
print(bool(1))         # True，非零数被认为是True
print(bool(""))        # False，空字符串被认为是False
print(bool("Hello"))   # True，非空字符串被认为是True

# 比较运算符
print(1 != 2)  # True，因为1不等于2
print(2 > 1)   # True，因为2大于1
print(2 < 1)   # False，因为2不小于1
print(2 >= 2)  # True，因为2大于等于2
print(2 <= 1)  # False，因为2不小于等于1