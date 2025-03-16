# 循环语句

# for循环语句优化
# 字符 - 使用enumerate
# enumerate函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
for index, char in enumerate('Hello Python'):
    print(f'位置 {index}: {char}')

# 字典遍历优化 - 使用items()
# items()方法返回一个包含字典所有键值对的视图对象，可以用来遍历字典的键和值
dict1 = {'a': '小学', 'b': '初中', 'c': '高中', 'd': '大学'}
for key, value in dict1.items():
    print(f'等级 {key}: {value}')

# rang() 函数, start, stop, step
# range(x) 生成从0到x-1的整数序列
# range(start, stop, step) 生成从start到stop-1，步长为step的整数序列

# range循环优化 - 使用列表推导式
# 列表推导式是一种简洁的创建列表的方式
numbers = [i for i in range(3)]
print(numbers)

# 带步长的列表推导式
numbers_step = [i for i in range(3, 6, 2)]
print(numbers_step)

# 条件列表推导式
even_numbers = [i for i in range(6) if i % 2 == 0]
print(even_numbers)

# While 循环语句
# for 适合已知循环次数或需要遍历序列（列表、元组、字符串等）的情况
# while 适合未知循环次数，需要根据条件判断是否继续循环的情况
count = 1
sum1 = 0
while count <= 100:
    sum1 = sum1 + count
    count = count + 1
print(sum1)

# 嵌套循环
# for嵌套循环
# 嵌套循环是指一个循环体内再包含另一个完整的循环结构
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(i, j, i*j), end='')  
    print()
# while嵌套循环
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('{}x{}={}\t'.format(i, j, i*j), end='') 
        j = j + 1
    print()
    i = i + 1

# 循环控制语句
# break 终止循环，并且跳出整个循环
for i in range(1, 10):
    if i == 5:
        break
    else:
        print(i)
# continue 跳出该次循环，执行下一次循环
for i in range(1, 10):
    if i == 5:
        continue
    else:
        print(i)
# pass 不做任何事情，一般用作占位语句
for i in range(1, 10):
    if i == 5:
        pass  # 占位语句，什么都不做
    else:
        print(i)

# 例子: 判断是否闰年
# 闰年判断规则：能被4整除但不能被100整除，或者能被400整除的年份
year = int(input('请输入年份：'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('{}是闰年'.format(year))
else:
    print('{}不是闰年'.format(year))