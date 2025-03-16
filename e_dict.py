# 字典 (Dictionary) 
# 类似JAVA中的Map

# 字典的创建
dict1 = {'LiLei': '111111', 'HanMeiMei': '222222', 'MaDong': '333333'}
dict1 = {'abc': 123, 123: 'abc'}

# 访问字典
dict2 = {'LiLei': '131456780001', 'HanMeiMei': '131456780002', 'MaDong': '131456780003', 'LiNing': '131456780004', 'JiKe': '131456780005'}
print(dict2['HanMeiMei'])  # 输出: 131456780002

# 修改字典
dict3 = {'LiLei': '111111', 'HanMeiMei': '222222', 'MaDong': '333333'}
print(dict3)
# 新增一个键值对
dict3['Jack'] = '444444'
print(dict3)
# 修改键值对
dict3['MaDong'] = '555555'
print(dict3)

# 删除字典元素
dict4 = {'LiLei': '111111', 'HanMeiMei': '222222', 'MaDong': '333333'}
print(dict4)
# 通过 key 值，删除对应的元素
del dict4['MaDong']
print(dict4)
# 删除字典中的所有元素
dict4.clear()
print(dict4)
# 删除字典
del dict4

# 字典使用注意项
# 1. 键不可重复，如果重复，后面的会覆盖前面的
dict5 = {'LiLei': '111111', 'HanMeiMei': '222222', 'MaDong': '333333', 'XiaXiao': '444444'}
print(dict5)  # 输出: {'LiLei': '111111', 'HanMeiMei': '222222', 'MaDong': '333333', 'XiaXiao': '444444'}
print(dict5['XiaXiao'])  # 输出: 444444
# 2. 键必须是不可变的对象，比如字符串，数字或元组，而列表是可变的，不能作为键
dict6 = {'LiLei': '111111', 'HanMeiMei': '222222', (123, 'Tom'): '333333', 'XiaXiao': '444444'}
print(dict6)
# 3. 字典是无序的，不能用下标访问
# 查找效率高，不会随着key的增加而变慢
# 缺点占用内存大

dict7 = {'LiLei': '111111', 'HanMeiMei': '222222', 'MaDong': '333333'}
# 字典内置函数&方法
# len(dict) 计算字典元素个数，即键的总数
print(len(dict7))  # 输出: 3
# str(dict) 输出字典，以可打印的字符串表示
print(str(dict7))  # 输出: {'LiLei': '111111', 'HanMeiMei': '222222', 'MaDong': '333333'}
# type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型
print(type(dict7))  # 输出: <class 'dict'>
# dict.clear() 删除字典内所有元素
dict7.clear()
print(dict7)  # 输出: {}
# dict.copy() 返回一个字典的浅复制
dict8 = dict6.copy()
# dict.values() 以列表返回字典中的所有值
print(dict8.values())  # 输出: dict_values(['111111', '222222', '333333', '444444'])
# dict.keys() 以列表返回一个字典所有的键
print(dict8.keys())  # 输出: dict_keys(['LiLei', 'HanMeiMei', (123, 'Tom'), 'XiaXiao'])
# dict.items() 以列表返回可遍历的(键, 值) 元组数组
print(dict8.items())  # 输出: dict_items([('LiLei', '111111'), ('HanMeiMei', '222222'), ((123, 'Tom'), '333333'), ('XiaXiao', '444444')])
# dict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值 
print(dict8.get('AnWen', 'not found'))  # 输出: not found
# dict.pop() 随机返回并删除字典中的一对键和值(一般删除末尾对)
print(dict8.pop('LiLei'))  # 输出: 111111
# dict.popitem() 随机返回并删除字典中的一对键和值
print(dict8.popitem())  # 输出: ('HanMeiMei', '222222')
print(dict8)