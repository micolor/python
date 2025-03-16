# Python列表生成式（List Comprehension）详解
# -------------------------------------------

# 1. 基础列表生成
# 生成1-30的列表
list1 = list(range(1,31))
print("基础列表:", list1)

# 2. 九九乘法表（使用列表生成式）
# 使用嵌套的列表生成式，外层控制行，内层控制列
print("九九乘法表：")
print('\n'.join([ ' '.join('%dx%d=%2d' % (x,y,x * y) for x in range(1, y + 1)) for y in range(1, 10) ]))
print('\n'.join([ ' '.join('%dx%d=%2d' % (x,y,x * y) for y in range(x, 10)) for x in range(1, 10) ]))

# 3. 列表生成式的基本语法
# 单条件列表生成式: [表达式 for 变量 in 可迭代对象]
# 带条件列表生成式: [表达式 for 变量 in 可迭代对象 if 条件]

# 示例3.1：计算1-10的平方
list1=[x * x for x in range(1, 11)]
print("1-10的平方:", list1)

# 示例3.2：计算1-10中偶数的平方
list2=[x * x for x in range(1, 11) if x % 2 == 0]
print("偶数的平方:", list2)

# 示例3.3：使用双重循环生成坐标对
list3 = [(x + 1, y + 1) for x in range(3) for y in range(5)]
print("坐标对:", list3)

# 示例3.4：生成字母列表
letters = [chr(x) for x in range(65, 91)]
print("大写字母表:", letters)

# 示例3.5：列表元素处理
words = ['Hello', 'World', 'Python']
lengths = [len(word) for word in words]
print("单词长度:", lengths)

# 4. 列表生成式的高级用法
# 示例4.1：嵌套列表生成式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("展开的矩阵:", flattened)

# 示例4.2：条件嵌套列表生成式
even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]
print("矩阵中的偶数:", even_matrix)

# 示例4.3：带多个条件的列表生成式
filtered_list = [x for x in range(1, 31) if x % 2 == 0 if x % 3 == 0]
print("同时被2和3整除的数:", filtered_list)

# 5. 列表生成式与函数结合
# 示例5.1：结合函数生成列表
def square(x):
    return x * x

squares = [square(x) for x in range(1, 11)]
print("使用函数计算平方:", squares)

# 示例5.2：结合lambda函数生成列表
cubes = [(lambda x: x ** 3)(x) for x in range(1, 11)]
print("使用lambda函数计算立方:", cubes)