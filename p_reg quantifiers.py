# 数量词
# 贪婪	惰性	描述
# ?		??		0 或 1 次，等价于 {0,1}
# +		+?		1 次或更多，等价于 {1,}
# *		*?		0 次或更多，等价于 {0,}
# {n}	{n}?	恰好 n 次
# {n,m}	{n,m}?	至少 n 次，至多 m 次
# {n,}	{n}?	至少 n 次

import re
a = 'java*&39android##@@python'

# 贪婪数量词示例
findall_greedy = re.findall('[a-z]{4,7}', a)
print("贪婪数量词:", findall_greedy)

# 惰性数量词示例
findall_lazy = re.findall('[a-z]{4,7}?', a)
print("惰性数量词:", findall_lazy)

# 其他数量词示例
b = 'a aa aaa aaaa aaaaa'
findall_zero_or_one = re.findall('a{0,1}', b)
print("0 或 1 次:", findall_zero_or_one)

findall_one_or_more = re.findall('a{1,}', b)
print("1 次或更多:", findall_one_or_more)

findall_zero_or_more = re.findall('a{0,}', b)
print("0 次或更多:", findall_zero_or_more)

findall_exactly_n = re.findall('a{3}', b)
print("恰好 3 次:", findall_exactly_n)

findall_at_least_n = re.findall('a{2,}', b)
print("至少 2 次:", findall_at_least_n)

findall_between_n_and_m = re.findall('a{2,4}', b)
print("至少 2 次，至多 4 次:", findall_between_n_and_m)