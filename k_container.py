"""Python自定义容器教程

1. 容器基础知识
-------------
● 不可变容器(tuple): 
  - 只需实现: __len__, __getitem__
  - 特点: 创建后内容不可修改

● 可变容器(list/dict/set): 
  - 需实现: __len__, __getitem__, __setitem__, __delitem__
  - 特点: 可以修改、删除元素

2. 关键方法说明
-------------
__len__(self)        # 返回容器长度
__getitem__(self,k)  # 实现 container[key] 取值
__setitem__(self,k,v)# 实现 container[key]=value 赋值
__delitem__(self,k)  # 实现 del container[key] 删除
__iter__(self)       # 实现迭代功能 for x in container

3. 使用示例
-------------
# 创建自定义列表
fl = FunctionalList([1,2,3,4,5])
fl.head()    # 获取首元素: 1
fl.tail()    # 获取除首元素外的列表: [2,3,4,5]
fl.take(2)   # 获取前2个元素: [1,2]
fl.drop(2)   # 删除前2个元素后的列表: [3,4,5]
"""

class FunctionalList(object):
    '''
    功能性列表类：实现了内置类型list的基本功能，并扩展了函数式编程相关的方法
    
    主要特性：
    1. 支持所有基础的列表操作（获取长度、索引访问、修改、删除等）
    2. 支持迭代和反向迭代
    3. 提供函数式编程常用方法：head、tail、init、last、drop、take
    
    基本用法：
    fl = FunctionalList([1,2,3,4,5])
    print(fl.head())  # 获取第一个元素：1
    print(fl.tail())  # 获取除第一个外的所有元素：[2,3,4,5]
    '''
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return FunctionalList(reversed(self.values))

    def append(self, value):
        self.values.append(value)

    def head(self):
        """获取第一个元素，如果列表为空则抛出异常"""
        if not self.values:
            raise ValueError("不能对空列表执行head操作")
        return self.values[0]

    def tail(self):
        """获取除第一个元素外的所有元素
        返回：list类型
        """
        if not self.values:
            raise ValueError("不能对空列表执行tail操作")
        return self.values[1:]

    def init(self):
        """获取除最后一个元素外的所有元素
        返回：list类型
        """
        if not self.values:
            raise ValueError("不能对空列表执行init操作")
        return self.values[:-1]

    def last(self):
        """获取最后一个元素，如果列表为空则抛出异常"""
        if not self.values:
            raise ValueError("不能对空列表执行last操作")
        return self.values[-1]

    def drop(self, n):
        """获取去除前n个元素后的所有元素
        参数：
            n: int类型，需要去除的元素个数
        返回：list类型
        """
        if not isinstance(n, int):
            raise TypeError("n必须是整数类型")
        if n < 0:
            raise ValueError("n不能为负数")
        return self.values[n:]

    def take(self, n):
        """获取前n个元素
        参数：
            n: int类型，需要获取的元素个数
        返回：list类型
        """
        if not isinstance(n, int):
            raise TypeError("n必须是整数类型")
        if n < 0:
            raise ValueError("n不能为负数")
        return self.values[:n]
