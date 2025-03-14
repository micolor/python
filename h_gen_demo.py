# 迭代器和生成器的综合例子

# 反向迭代
list1 = [1, 2, 3, 4, 5]
for num1 in list1:
    print(num1, end=' ')

list1 = [1, 2, 3, 4, 5]
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

for rr in Countdown(10):
    print(rr)
for rr in Countdown(30):
    print(rr)

# zip()函数
# 同时迭代多个序列
# zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中 x 来自 a，y 来自 b。
# 一旦其中某个序列到底结尾，迭代宣告结束。因此迭代长度跟参数中最短序列长度一致。
names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19, 20]
sex = ['男', '女', '男']
for name, age, sex in zip(names, ages, sex):
    print(name, age, sex)

# 利用zip()生成字典
names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19, 20]
dict1 = dict(zip(names, ages))
print(dict1)