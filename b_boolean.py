# 布尔值
print(1 == 1)  # True，因为1等于1
print(1 == 2)  # False，因为1不等于2

# 布尔值与其他数据类型
print(bool(0))         # False，0被认为是False
print(bool(1))         # True，非零数被认为是True
print(bool(""))        # False，空字符串被认为是False
print(bool("Hello"))   # True，非空字符串被认为是True
print(bool({}))        # False，空字典被认为是False
print(bool(None))      # False，None被认为是False
print(bool([]))        # False，空列表被认为是False
print(bool([1, 2, 3])) # True，非空列表被认为是True
print(bool({"key": "value"}))  # True，非空字典被认为是True

# 布尔运算符
print(True and False)  # False，因为and运算符要求两个操作数都为True
print(True or False)   # True，因为or运算符只要求一个操作数为True
print(not True)        # False，因为not运算符取反

# 布尔运算符的优先级
print(True or False and False)  # True，因为and的优先级高于or，相当于True or (False and False)
print((True or False) and False)  # False，因为括号改变了优先级，相当于(True or False) and False

# 比较运算符
print(1 != 2)  # True，因为1不等于2
print(2 > 1)   # True，因为2大于1
print(2 < 1)   # False，因为2不小于1
print(2 >= 2)  # True，因为2大于等于2
print(2 <= 1)  # False，因为2不小于等于1
print(1 == 1.0)  # True，因为1等于1.0
print("a" < "b")  # True，因为在字母表中a在b之前
print("abc" > "ab")  # True，因为字符串比较是逐字符进行的