# yield 关键字

# yield 是一个生成器函数，用于在函数中返回一个值，并在下次调用时从上次返回的地方继续执行。
# 它允许函数生成一个序列的值，而不是一次性返回一个完整的序列。

# 经典案例：斐波那契数列生成器
def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        yield a
        a, b = b, a + b
        n -= 1

# 使用生成器
for num in fibonacci(10):
    print(num)

# 解释：
# 1. 定义了一个生成器函数 fibonacci，它使用 yield 关键字返回斐波那契数列中的值。
# 2. 每次调用生成器时，它会从上次返回的地方继续执行，直到生成器函数结束或遇到下一个 yield 语句。
# 3. 使用 for 循环遍历生成器，打印前 10 个斐波那契数。

# 补充知识点：
# 1. 生成器函数与普通函数的区别在于，生成器函数使用 yield 关键字，而普通函数使用 return 关键字。
# 2. 生成器函数在每次调用时不会重新开始，而是从上次离开的地方继续执行。
# 3. 生成器函数返回的是一个迭代器对象，可以使用 next() 函数获取下一个值。
# 4. 生成器函数可以使用 for 循环遍历，或者使用 list() 函数将其转换为列表。

# 示例：使用 next() 函数获取生成器的值
gen = fibonacci(5)
print(next(gen))  # 输出 0
print(next(gen))  # 输出 1
print(next(gen))  # 输出 1
print(next(gen))  # 输出 2
print(next(gen))  # 输出 3

# 示例：将生成器转换为列表
gen_list = list(fibonacci(5))
print(gen_list)  # 输出 [0, 1, 1, 2, 3]
