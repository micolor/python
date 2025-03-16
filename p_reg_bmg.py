# 边界匹配符和组
# ^    匹配字符串开头
# $    匹配字符串末尾
# \A   仅匹配字符串开头
# \Z   仅匹配字符串末尾
# \b   匹配 \w 和 \W 之间
# \B   匹配非单词边界
# (?=...) 正向肯定预查
# (?!...) 正向否定预查
# (?<=...) 反向肯定预查
# (?<!...) 反向否定预查
# (?:...) 非捕获组
# (?P<name>...) 命名捕获组
# (?P=name) 引用命名捕获组

import re

# 示例:
# ^: 匹配字符串开头
print(bool(re.findall(r'^hello', 'hello world')))  # 匹配
print(bool(re.findall(r'^hello', 'world hello')))  # 不匹配

# $: 匹配字符串的末尾
print(bool(re.findall(r'world$', 'hello world')))  # 匹配
print(bool(re.findall(r'world$', 'world hello')))  # 不匹配

# \A: 仅匹配字符串开头
print(bool(re.findall(r'\Ahello', 'hello world')))  # 匹配
print(bool(re.findall(r'\Ahello', 'world hello')))  # 不匹配

# \Z: 仅匹配字符串末尾
print(bool(re.findall(r'world\Z', 'hello world')))  # 匹配
print(bool(re.findall(r'world\Z', 'world hello')))  # 不匹配

# \b: 匹配 \w 和 \W 之间
print(bool(re.findall(r'\bcat\b', 'a cat in the hat')))  # 匹配
print(bool(re.findall(r'\bcat\b', 'concatenate')))  # 不匹配

# \B: 匹配非单词边界
print(bool(re.findall(r'\Bcat\B', 'concatenate')))  # 匹配
print(bool(re.findall(r'\Bcat\B', 'a cat in the hat')))  # 不匹配

# (?=...): 正向肯定预查
print(bool(re.findall(r'foo(?=bar)', 'foobar')))  # 匹配
print(bool(re.findall(r'foo(?=bar)', 'foobaz')))  # 不匹配

# (?!...): 正向否定预查
print(bool(re.findall(r'foo(?!bar)', 'foobaz')))  # 匹配
print(bool(re.findall(r'foo(?!bar)', 'foobar')))  # 不匹配

# (?<=...): 反向肯定预查
print(bool(re.findall(r'(?<=foo)bar', 'foobar')))  # 匹配
print(bool(re.findall(r'(?<=foo)bar', 'bazbar')))  # 不匹配

# (?<!...): 反向否定预查
print(bool(re.findall(r'(?<!foo)bar', 'bazbar')))  # 匹配
print(bool(re.findall(r'(?<!foo)bar', 'foobar')))  # 不匹配

# (?:...): 非捕获组
print(bool(re.findall(r'(?:foo)bar', 'foobar')))  # 匹配
print(bool(re.findall(r'(?:foo)bar', 'foobaz')))  # 不匹配

# (?P<name>...): 命名捕获组
match = re.search(r'(?P<word>\w+)', 'hello world')
if match:
    print(match.group('word'))  # 输出 'hello'

# (?P=name): 引用命名捕获组
print(bool(re.findall(r'(?P<word>\w+)\s+(?P=word)', 'hello hello')))  # 匹配
print(bool(re.findall(r'(?P<word>\w+)\s+(?P=word)', 'hello world')))  # 不匹配

