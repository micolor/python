# 迭代器和生成器的综合例子

# 反向迭代
list1 = [1, 2, 3, 4, 5]
print("正向迭代:")
for num1 in list1:
    print(num1, end=' ')

print("\n反向迭代:")
for num1 in reversed(list1):
    print(num1, end=' ')

print('\n')

# 自定义__reversed__()
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # 正向迭代器
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        # 反向迭代器
        n = 1
        while n <= self.start:
            yield n
            n += 1

print("Countdown 正向迭代:")
for rr in Countdown(10):
    print(rr, end=' ')
print("\nCountdown 反向迭代:")
for rr in reversed(Countdown(10)):
    print(rr, end=' ')

print('\n')

# zip()函数
# 同时迭代多个序列
# zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中 x 来自 a，y 来自 b。
# 一旦其中某个序列到底结尾，迭代宣告结束。因此迭代长度跟参数中最短序列长度一致。
names = ['PP', 'YY', 'TT']
ages = [18, 19, 20]
sex = ['男', '女', '男']
print("使用 zip() 同时迭代多个序列:")
for name, age, sex in zip(names, ages, sex):
    print(name, age, sex)

# 利用zip()生成字典
names = ['PP', 'YY', 'TT']
ages = [18, 19, 20]
dict1 = dict(zip(names, ages))
print("利用 zip() 生成字典:")
print(dict1)

# 生成器表达式
# 生成器表达式与列表推导式类似，但生成器表达式返回一个生成器对象，而不是一个列表。
print("生成器表达式:")
gen_exp = (x * x for x in range(10))
for x in gen_exp:
    print(x, end=' ')

print('\n')