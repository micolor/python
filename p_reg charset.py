# 字符集
import re
a = 'uav,ubv,ucv,uwv,uzv,ucv,uov'

# 取 u 和 v 中间是 a 或 b 或 c 的字符
findall = re.findall('u[abc]v', a)
print(findall)
# 如果是连续的字母，数字可以使用 - 来代替
l = re.findall('u[a-c]v', a)
print(l)

# 取 u 和 v 中间不是 a 或 b 或 c 的字符
re_findall = re.findall('u[^abc]v', a)
print(re_findall)

# 概括字符集
b = 'uav_ubv_ucv_uwv_uzv_ucv_uov&123-456-789'
# \d 匹配所有数字字符，相当于 [0-9]
findall1 = re.findall('\d', b)
# [0-9] 匹配所有数字字符
findall2 = re.findall('[0-9]', b)
# \D 匹配所有非数字字符，相当于 [^0-9]
findall3 = re.findall('\D', b)
# [^0-9] 匹配所有非数字字符
findall4 = re.findall('[^0-9]', b)
print(findall1)
print(findall2)
print(findall3)
print(findall4)

# \w 匹配包括下划线的任何单词字符，等价于 [A-Za-z0-9_]
findall5 = re.findall('\w', b)
# [A-Za-z0-9_] 匹配包括下划线的任何单词字符
findall6 = re.findall('[A-Za-z0-9_]', b)
print(findall5)
print(findall6)

# \W 匹配任何非单词字符，相当于 [^A-Za-z0-9_]
findall7 = re.findall('\W', b)
# [^A-Za-z0-9_] 匹配任何非单词字符
findall8 = re.findall('[^A-Za-z0-9_]', b)
print(findall7)
print(findall8)

# \s 匹配任何空白字符，相当于 [ \t\n\r\f\v]
findall9 = re.findall('\s', b)
# [ \t\n\r\f\v] 匹配任何空白字符
findall10 = re.findall('[ \t\n\r\f\v]', b)
print(findall9)
print(findall10)

# \S 匹配任何非空白字符，相当于 [^ \t\n\r\f\v]
findall11 = re.findall('\S', b)
# [^ \t\n\r\f\v] 匹配任何非空白字符
findall12 = re.findall('[^ \t\n\r\f\v]', b)
print(findall11)
print(findall12)