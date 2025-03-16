# re.sub
# pattern	表示正则中的模式字符串
# repl	repl，就是replacement，被替换的字符串的意思，可以是字符串或函数
# string	即表示要被处理，要被替换的那个 string 字符串
# count	对于pattern中匹配到的结果，count可以控制对前几个group进行替换，默认为0表示替换所有匹配
# flags	正则表达式修饰符，例如 re.IGNORECASE 表示忽略大小写

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re

a = 'Python*Android*Java-888'

# 把字符串中的 * 字符替换成 & 字符
sub1 = re.sub(r'\*', '&', a)
print(sub1)  # 输出: Python&Android&Java-888

# 把字符串中的第一个 * 字符替换成 & 字符
sub2 = re.sub(r'\*', '&', a, 1)
print(sub2)  # 输出: Python&Android*Java-888

# 把字符串中的 * 字符替换成 & 字符,把字符 - 换成 |
# 1、先定义一个函数
def convert(value):
    group = value.group()
    if group == '*':
        return '&'
    elif group == '-':
        return '|'

# 第二个参数，要替换的字符可以为一个函数
sub3 = re.sub(r'[\*-]', convert, a)
print(sub3)  # 输出: Python&Android&Java|888

# 使用 flags 参数忽略大小写
b = 'Python*android*Java-888'
sub4 = re.sub(r'android', 'Android', b, flags=re.IGNORECASE)
print(sub4)  # 输出: Python*Android*Java-888