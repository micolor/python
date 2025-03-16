# 变量

# 变量的创建和赋值
# Python 是动态类型语言，变量可以指向不同类型的对象
a = 'hello python'
print(a)  # 输出: hello python
a = 123
print(a)  # 输出: 123

# 变量的指向问题
# 变量名只是对象的引用，可以重新指向其他对象
a = 'hello python'
b = a  # b 和 a 指向相同的对象
a = 123  # a 重新指向新的对象
print(b)  # 输出: hello python

# 多个变量赋值
# 可以同时为多个变量赋相同的值
a = b = c = 123  # 所有变量指向相同的对象
print(a)  # 输出: 123

# 也可以在一行中为多个变量赋不同的值
a, b, c = 1, 2, 3  # 多个变量同时赋值
print(a)  # 输出: 1
print(b)  # 输出: 2
print(c)  # 输出: 3