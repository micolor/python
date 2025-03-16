# Python函数教程
# -------------

# 函数定义的基本语法:
# def 函数名(参数1，参数2....参数n):
#     函数体
#     return 语句

# 函数的返回值
def sum(num1, num2):
    """返回两个数的和"""
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError('参数类型错误')
    return num1 + num2

print(sum(1, 2))

# 返回多个值
def division(dividend, divisor):
    """返回商和余数"""
    remainder = dividend % divisor
    quotient = (dividend - remainder) / divisor
    return quotient, remainder

quotient, remainder = division(9, 4)
result_tuple = division(9, 4)
print(quotient, remainder)
print(result_tuple)

# 函数的参数
# 默认参数
def print_user_info(name, age, sex='男'):
    """打印用户信息"""
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return

print_user_info('小芳', 18, '女')
print_user_info('小明', 18)

# 默认值是引用类型时，函数调用时会发生什么
def test_default_param(param1, param2=None):
    """测试默认参数的行为"""
    if param2 is None:
        param2 = []
    print('param1:', param1)
    print('param2:', param2)
    return param2

result = test_default_param([1, 2, 3])
result.append('error')
test_default_param([1, 2, 3])

# 关键字参数
# 可以通过参数名来给函数传递参数，而不用关心参数列表定义时的顺序
print_user_info(sex='女', age=18, name='小芳')

# 不定长参数
# *hobbies是可变参数，且 hobbies 其实就是一个 tuple （元祖）
def print_user_info_with_hobbies(name, age, sex='男', *hobbies):
    """打印用户信息和爱好"""
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    print('爱好：{}'.format(hobbies))
    return

print_user_info_with_hobbies('小芳', 18, '女', '打球', '看电影', '看小说')

# **hobbies是关键字参数，且 hobbies 其实是一个 dict（字典）
def print_user_info_with_keywords(name, age, sex='男', **hobbies):
    """打印用户信息和爱好"""
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    print('爱好：{}'.format(hobbies))
    return

print_user_info_with_keywords('小芳', 18, '女', sport='打球', movie='看电影', novel='看小说')

# 只接受关键字参数
# age , sex 不使用关键字参数是会报错
def print_user_info_with_keywords_only(name, *, age, sex='男'):
    """打印用户信息，仅接受关键字参数"""
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return

# 调用 print_user_info 函数
print_user_info_with_keywords_only(name='小芳', age=18, sex='女')
print_user_info_with_keywords_only('小芳', age='22', sex='男')

# 函数传值问题
def change_number(b):
    """改变数值"""
    b = 1000

b = 1
change_number(b)
print(b)

# 在 Python 中，字符串，整形，浮点型，tuple 是不可更改的对象，而list，dict 等是可以更改的对象
# 变量赋值 a = 1，其实就是生成一个整形对象 1 ，然后变量 a 指向 1，当 a = 1000 其实就是再生成一个整形对象 1000，然后改变 a 的指向，不再指向整形对象 1 ，而是指向 1000，最后 1 会被丢弃
def change_list(b):
    """改变列表"""
    b.append(1000)

b = [1, 2, 3, 4, 5]
change_list(b)
print(b)

# 匿名函数
# 基本语法
# lambda 参数1，参数2...参数n : 函数体
sum_lambda = lambda num1, num2: num1 + num2
print(sum_lambda(1, 2))

# 在运行时绑定值，而不是定义时就绑定
num2 = 100
sum1 = lambda num1: num1 + num2

num2 = 10000
sum2 = lambda num1: num1 + num2

print(sum1(1))
print(sum2(1))