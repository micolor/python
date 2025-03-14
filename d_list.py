# -*- coding: utf-8 -*-
# List（列表）

# 初始化列表
names = ['一点水', '二点水', '三点水', '四点水', '五点水']
print(names)

# 列表的数据元素不一定是相同的数据类型
list1 = ['两点水', 'twowter', 'liangdianshui', 123]
print(list1)
# 通过索引来访问列表中的元素
print(list1[0])
# 通过方括号的形式来截取列表中的数据, 左闭右开区间，从第0个元素开始取2个元素
print(list1[0:2])
# 通过索引对列表的数据项进行修改或更新
list1[1] = '2点水'
# 使用 append() 方法来添加列表项
list1.append('六点水')
print(list1)
# 删除列表中的元素
del list1[3]
print(list1)


# list运算符
# 计算列表元素个数
print(len([1, 2, 3]))
# 连接两个列表
print([1, 2, 3] + [4, 5, 6])
# 复制列表
print(['Hi!'] * 4)
# 判断元素是否存在于列表中
print(3 in [1, 2, 3])
# 迭代列表
for x in [1, 2, 3]:
    print(x)


# list 函数&方法
# len(list) 计算列表元素个数 
print(len([1, 2, 3]))
# max(list) 返回列表元素最大值
print(max([1, 2, 3]))
# min(list) 返回列表元素最小值
print(min([1, 2, 3]))
# list(seq) 将元组转换为列表
print(list(names))
# list.append(obj) 在列表末尾添加新的对象
names.append('六点水')
print(names)
# list.count(obj) 统计某个元素在列表中出现的次数
print(names.count('一点水'))
# list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值
names.extend(['七点水', '八点水'])
print(names)
# list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
print(names.index('一点水'))
# list.insert(index, obj) 将对象插入列表
names.insert(1, '一点水')
print(names)
# list.pop(obj=list[-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(names.pop())
# list.remove(obj) 移除列表中某个值的第一个匹配项, 无返回值
names.remove('一点水')
print(names)
# list.reverse() 反向列表中元素
names.reverse()
print(names)
# list.sort([func]) 对原列表进行排序
names.sort()
print(names)


# 例子
print("==================x=======================")
user = ['liangdianshui', 'twowater', '两点水']
print(user)

# 统计列表中元素的个数
print(len(user))
# 根据索引获取列表中的元素
print(user[0] + ',' + user[1] + ',' + user[2])
# 末尾追加元素
user.append('three water')
print(user)
# 删除末尾元素
user.pop()
print(user)
# 删除指定位置的元素
user.pop(1)
print(user)
# 修改指定位置的元素
user[1] = 'two water'
print(user)
# 多维列表
new_user = [['VIP用户', 11111], ['twowater', 22222], ['三点水', 33333]]
print(new_user)