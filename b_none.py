# 空值
# 在 Python 中，空值用 None 表示。None 是一个特殊的常量，表示没有值或空值。
# 它不是 0，也不是空字符串，它是一个独立的类型：NoneType。
# None 常用于表示缺少值的情况，例如函数没有返回值时，默认返回 None。

# 示例：打印 None
print(None)

# 示例：函数没有返回值时，默认返回 None
def no_return():
    pass

result = no_return()
print(result)  # 输出: None

# 示例：检查变量是否为 None
a = None
if a is None:
    print("a 是 None")
else:
    print("a 不是 None")