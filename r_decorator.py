# 说明装饰器的作用
# 装饰器用于在不修改原函数代码的情况下，增加额外的功能
# 例如，在调用原函数前打印当前时间

# 装饰器示例
import time

# 装饰器函数
def decorator(func):
    def wrapper(*args, **kwargs):
        print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        func(*args, **kwargs)
    return wrapper

# 使用装饰器装饰 punch 函数
@decorator
def punch(name, department):
    print('昵称：{0}  部门：{1} 上班打卡成功'.format(name, department))

# 使用装饰器装饰 print_args 函数
@decorator
def print_args(reason, **kwargs):
    print(reason)
    print(kwargs)

# 调用装饰后的函数
punch('AnWen', '信息部')
print_args('AnWen', sex='男', age=99)

# 装饰器的详细讲解
# 1. 装饰器本质上是一个函数，它可以让其他函数在不修改代码的情况下增加额外的功能。
# 2. 装饰器函数接受一个函数作为参数，并返回一个新的函数。
# 3. 在新的函数中，可以在调用原函数之前或之后添加额外的代码。
# 4. 使用 @decorator 语法糖，可以方便地将装饰器应用到函数上。

# 示例：记录函数执行时间的装饰器
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间：{end_time - start_time} 秒")
        return result
    return wrapper

@timeit
def example_function():
    time.sleep(2)
    print("函数执行完毕")

example_function()

# 总结：
# - 装饰器用于在不修改原函数代码的情况下，增加额外的功能。
# - 装饰器函数接受一个函数作为参数，并返回一个新的函数。
# - 使用 @decorator 语法糖，可以方便地将装饰器应用到函数上。
# - 装饰器可以用于记录日志、性能测试、事务处理等场景。

