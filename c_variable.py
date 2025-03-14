# 变量

# 变量的创建和赋值
a = 'hello python'
print(a)  # 输出: hello python
a = 123
print(a)  # 输出: 123

# 变量的指向问题
a = 'hello python'
b = a  # b 指向与 a 相同的对象
a = 123  # a 指向新的对象
print(b)  # 输出: hello python

# 多个变量赋值
a = b = c = 123  # 所有变量指向相同的对象
print(a)  # 输出: 123
a, b, c = 1, 2, 3  # 多个变量同时赋值
print(a)  # 输出: 1
print(b)  # 输出: 2
print(c)  # 输出: 3