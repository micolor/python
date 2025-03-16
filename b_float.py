# 浮点数
# 浮点数的精度问题
print(0.55 + 0.41)  # 0.96
print(0.55 + 0.4)   # 0.9500000000000001
print(0.55 + 0.411) # 0.9610000000000001
# 因为计算机对浮点数的表达本身是不精确的。保存在计算机中的是二进制数，二进制对有些数字不能准确表达，只能非常接近这个数。

# 使用round函数来减少浮点数误差
print(round(0.55 + 0.4, 2))  # 0.95
print(round(0.55 + 0.411, 2))  # 0.96

# 浮点数的科学计数法表示
print(1.23e4)  # 12300.0
print(1.23e-4)  # 0.000123

# 浮点数的类型转换
print(float(1))  # 1.0
print(float("3.14"))  # 3.14

# 使用round函数来减少浮点数误差
print(round(0.1 + 0.2, 2))  # 0.3
print(round(0.1 * 0.1, 2))  # 0.01

from decimal import Decimal
# 使用decimal模块来减少浮点数误差
print(Decimal('0.1') + Decimal('0.2'))  # 0.3
print(Decimal('0.1') * Decimal('0.1'))  # 0.01

# 浮点数比较
print(0.1 + 0.2 == 0.3)  # False
print(round(0.1 + 0.2, 2) == 0.3)  # True
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))  # True