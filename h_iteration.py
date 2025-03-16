# 迭代

# for 循环迭代字符串
for i in 'hello':
    print(i, end=' ')
print('\n')

# for 循环迭代 list
list1 = [1, 2, 3, 4, 5]
for i in list1:
    print(i, end=' ')
print('\n')

# for 循环迭代字典
dict1 = {'name': 'zhangsan', 'age': 18, 'sex': '男'}
for key in dict1:
    print(key, end=' ')
print('\n')
for value in dict1.values():
    print(value, end=' ')
print('\n')
for key, value in dict1.items():
    print(f'{key}: {value}', end=' ')
print('\n')

# for 循环迭代元组
tuple1 = ('a', 'b', 'c', 'd', 'e')
for i in tuple1:
    print(i, end=' ')
print('\n')

# for 循环迭代list元组
list2 = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for x, y in list2:
    print(x, y)
print('\n')

# 迭代器
# 字符串创建迭代器
str1 = 'hello'
iter1 = iter(str1)
# list 创建迭代器
list1 = [1, 2, 3, 4, 5]
iter2 = iter(list1)
# tuple 创建迭代器
tuple1 = ('a', 'b', 'c', 'd', 'e')
iter3 = iter(tuple1)
# 字典创建迭代器
dict1 = {'name': 'zhangsan', 'age': 18, 'sex': '男'}
iter4 = iter(dict1)

for i in iter1:
    print(i, end=' ')
print('\n')

for i in iter2:
    print(i, end=' ')
print('\n')

for i in iter4:
    print(i, end=' ')
print('\n')

# next() 函数遍历迭代器
while True:
    try:
        print(next(iter3), end=' ')
    except StopIteration:
        break
print('\n')

# 使用 enumerate() 函数进行索引迭代
list3 = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(list3):
    print(f'Index: {index}, Value: {value}')
print('\n')

# 使用 zip() 函数同时迭代多个序列
list4 = [1, 2, 3]
list5 = ['a', 'b', 'c']
for num, char in zip(list4, list5):
    print(f'Number: {num}, Character: {char}')
print('\n')

# 使用 reversed() 函数反向迭代
list6 = [1, 2, 3, 4, 5]
for i in reversed(list6):
    print(i, end=' ')
print('\n')

# 使用 sorted() 函数排序后迭代
list7 = [3, 1, 4, 1, 5, 9]
for i in sorted(list7):
    print(i, end=' ')
print('\n')