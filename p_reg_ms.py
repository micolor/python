# re.match 和 re.search 的区别:
# re.match 只能从字符串的起始位置匹配，而 re.search 则会扫描整个字符串，直到找到一个匹配。
# re.match 如果匹配成功，返回一个 Match 对象，否则返回 None。
# re.search 如果匹配成功，返回一个 Match 对象，否则返回 None。
# 示例代码:
import re

text = "Hello, world!"

# 使用 re.match
match = re.match("world", text)
if match:
    print("re.match 找到匹配:", match.group(0))
else:
    print("re.match 未找到匹配")

# 使用 re.search
search = re.search("world", text)
if search:
    print("re.search 找到匹配:", search.group(0))
else:
    print("re.search 未找到匹配")

# re.match 示例：从字符串起始位置匹配
match_start = re.match("Hello", text)
if match_start:
    print("re.match 从起始位置找到匹配:", match_start.group(0))
else:
    print("re.match 从起始位置未找到匹配")

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 提取图片的地址

import re

a = '<img src="https://s-media-cache-ak0.pinimg.com/originals/a8/c4/9e/a8c49ef606e0e1f3ee39a7b219b5c05e.jpg">'

# 使用 re.search
search = re.search('<img src="(.*)">', a)
# group(0) 是一个完整的分组
print(search.group(0))
print(search.group(1))

# 使用 re.findall
findall = re.findall('<img src="(.*)">', a)
print(findall)

# 多个分组的使用（比如我们需要提取 img 字段和图片地址字段）
re_search = re.search('<(.*) src="(.*)">', a)
# 打印 img
print(re_search.group(1))
# 打印图片地址
print(re_search.group(2))
# 打印 img 和图片地址，以元祖的形式
print(re_search.group(1, 2))
# 或者使用 groups
print(re_search.groups())


