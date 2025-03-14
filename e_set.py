# Set(集合)的基本操作演示
# set是Python中的无序不重复元素集合

# 1. 集合的创建
# set 的创建
# set 是一个无序不重复元素集
set1 = set([123, 456, 789])
print(set1)
set1=set([123,456,789,123,123])
print(set1)

# 2. 集合元素的添加
# set 添加元素
set2 = set([123, 456, 789])
print(set2)
set2.add(100)
print(set2)
set2.add(100)
print(set2)

# 3. 集合元素的删除
# set 删除元素
set3 = set([123, 456, 789])
print(set3)
set3.remove(123)
print(set3)

# 4. 集合运算示例
set4 = set('hello')
set5 = set(['p','y','y','h','o','n'])
print('集合4:', set4)
print('集合5:', set5)

# 4.1 交集运算(&): 获取两个集合中都包含的元素
set6 = set4 & set5
print('\n交集运算结果 (set4 & set5):', set6)

# 4.2 并集运算(|): 获取两个集合中所有的元素
set7 = set4 | set5
print('\n并集运算结果 (set4 | set5):', set7)

# 4.3 差集运算(-): 获取一个集合中有而另一个集合中没有的元素
set8 = set4 - set5  # set4中有而set5中没有的元素
set9 = set5 - set4  # set5中有而set4中没有的元素
print('\nset4对set5的差集:', set8)
print('set5对set4的差集:', set9)

# 5. 使用集合进行列表去重
set10 = set(['hello','hello','world','world'])
print('\n列表去重后的结果:', set10)