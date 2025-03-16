# 闭包教程

# 闭包是指在一个内部函数里，对外部作用域（但不是全局作用域）的变量进行引用，
# 然后把这个内部函数返回，相关的引用变量会和这个函数一同存在，即使外部函数已经结束。

def outer_function(outer_var):
    def inner_function(inner_var):
        return outer_var + inner_var
    return inner_function

# 创建闭包实例
closure_instance = outer_function(10)

# 调用闭包
print(closure_instance(5))  # 输出 15
print(closure_instance(20))  # 输出 30

# 解释：
# 在这个例子中，outer_function 是外部函数，inner_function 是内部函数。
# inner_function 引用了外部函数的变量 outer_var，并返回了 inner_function。
# 当我们调用 outer_function(10) 时，返回的闭包实例 closure_instance 记住了 outer_var 的值为 10。
# 无论何时调用 closure_instance，它都会使用这个记住的 outer_var 值。

# 在 Python 中，闭包中的变量是存储在 cell 对象的 cell_contents 属性中的。
# 我们可以通过 __closure__ 属性来访问这些 cell 对象。
print(closure_instance.__closure__[0].cell_contents)  # 输出 10

# 示例：计数器闭包
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

# 创建计数器闭包实例
counter1 = make_counter()
counter2 = make_counter()

# 调用计数器闭包
print(counter1())  # 输出 1
print(counter1())  # 输出 2
print(counter2())  # 输出 1
print(counter2())  # 输出 2

# 解释：
# 在这个例子中，make_counter 是外部函数，counter 是内部函数。
# counter 引用了外部函数的变量 count，并返回了 counter。
# 当我们调用 make_counter() 时，返回的闭包实例记住了 count 的初始值为 0。
# 每次调用闭包实例时，它都会更新并返回记住的 count 值。

# 同样，闭包中的变量 count 是存储在 cell 对象的 cell_contents 属性中的。
# 我们可以通过 __closure__ 属性来访问这些 cell 对象。
print(counter1.__closure__[0].cell_contents)  # 输出 2
print(counter2.__closure__[0].cell_contents)  # 输出 2

# 示例：带参数的闭包
def power_function(exponent):
    def power(base):
        return base ** exponent
    return power

# 创建平方和立方闭包实例
square = power_function(2)
cube = power_function(3)

# 调用闭包
print(square(3))  # 输出 9
print(cube(3))    # 输出 27

# 解释：
# 在这个例子中，power_function 是外部函数，power 是内部函数。
# power 引用了外部函数的变量 exponent，并返回了 power。
# 当我们调用 power_function(2) 时，返回的闭包实例 square 记住了 exponent 的值为 2。
# 当我们调用 power_function(3) 时，返回的闭包实例 cube 记住了 exponent 的值为 3。
# 无论何时调用 square 或 cube，它们都会使用各自记住的 exponent 值。

# 闭包的应用场景：
# 1. 数据隐藏：闭包可以用来创建私有变量，防止外部访问和修改。
# 2. 回调函数：闭包可以用作回调函数，保存状态信息。
# 3. 装饰器：闭包是实现装饰器的重要基础。

# 示例：数据隐藏
def make_account(initial_balance):
    balance = initial_balance
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            raise ValueError("Insufficient funds")
        balance -= amount
        return balance
    return deposit, withdraw

# 创建账户闭包实例
deposit, withdraw = make_account(100)

# 调用闭包
print(deposit(50))   # 输出 150
print(withdraw(30))  # 输出 120
print(withdraw(200)) # 抛出 ValueError: Insufficient funds