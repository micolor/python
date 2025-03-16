# 生成器

# 生成器的创建
# 使用生成器表达式创建生成器对象
gen = (x for x in range(10))
print(gen)  # 输出生成器对象

# 遍历生成器的元素
# 使用for循环遍历生成器中的元素
for num in gen:
    print(num)

# 以函数的形式实现生成器
# 使用yield关键字定义生成器函数
def gen_func():
    for i in range(10):
        yield i

gen = gen_func()
print(list(gen))  # 将生成器转换为列表并打印

# 斐波那契数列生成器
# 定义一个生成器函数来生成斐波那契数列
def fibon(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 打印前10个斐波那契数
for x in fibon(10):  
    print(x, end=' ')
print()  

# 奇数生成器
# generator 和函数的执行流程不一样。函数是顺序执行，遇到 return 语句或者最后一行函数语句就返回。
# 而变成 generator 的函数，在每次调用 next() 的时候执行，遇到 yield语句返回，再次执行时从上次返回的 yield 语句处继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o = odd()
print(next(o))  # 输出1并暂停
print(next(o))  # 输出3并暂停
print(next(o))  # 输出5并暂停

# 打印杨辉三角
# 定义一个生成器函数来生成杨辉三角的每一行
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break  # 打印前10行杨辉三角