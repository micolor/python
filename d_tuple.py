# -*- coding: utf-8 -*-
# tuple 元组
# tuple 元组和list相似，不同之处在于tuple的元素不能修改
# 能用tuple代替list就尽量用tuple

# 定义一个元组
tuple1 = ('twowater', '两点水', 'liangdianshui', 123)
tuple2 = 'twowater', '两点水', 'liangdianshui', 123
print(tuple1)
print(tuple2)

# 定义一个空元组
tuple3 = ()
print(tuple3)

# 定义一个只有一个元素的元组
# 元组中只包含一个元素时，需要在元素后面添加逗号
tuple4 = (123,)
print(tuple4)

# 注意：这不是一个元组，而是一个整数
tuple5 = (123)
print(tuple5)

# 访问元组
print(tuple1[0])
print(tuple2[1])

# 修改元组
# tuple 所谓的“不变”是说，tuple 的每个元素，指向永远不变
list1 = [123, 456]
tuple6 = ('twowater', '两点水', 'liangdianshui', list1)
print(tuple6)
list1[0] = 111
list1[1] = 222
print(tuple6)

# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tuple7 = ('twowater', '两点水', 'liangdianshui', 123)
print(tuple7)
del tuple7

# 元组运算符
# 计算元组元素个数
print(len((1, 2, 3)))
# 连接
print((1, 2, 3) + (4, 5, 6))
# 复制
print(('Hi!',) * 4)
# 元素是否存在
print(3 in (1, 2, 3))
# 迭代
for x in (1, 2, 3):
    print(x)

# 元组内置函数
# len(tuple) 计算元组元素个数
print(len((1, 2, 3)))
# max(tuple) 返回元组中元素最大值
print(max((1, 2, 3)))
# min(tuple) 返回元组中元素最小值
print(min((1, 2, 3)))
# tuple(seq) 将列表转换为元组
list2 = [1, 2, 3]
print(tuple(list2))