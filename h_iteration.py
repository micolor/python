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

# for 循环迭代元组
tuple1 = ('a', 'b', 'c', 'd', 'e')
for i in tuple1:
    print(i, end=' ')
print('\n')

# for 循环迭代list元组
list2 = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for x,y in list2:
    print (x , y)
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

for i in iter1:
    print(i, end=' ')
print('\n')

for i in iter2:
    print(i, end=' ')
print('\n')

# next() 函数遍历迭代器
while True:
    try:
        print(next(iter3), end=' ')
    except StopIteration:
        break