# 设定一个常量
a = '宇宙|地球|月球|火星|木星|jinxing'

# 判断是否有 宇宙 这个字符串，使用 PY 自带函数
print('是否含有宇宙这个字符串：{0}'.format(a.index('宇宙') > -1))
print('是否含有宇宙这个字符串：{0}'.format('宇宙' in a))

import re

# 正则表达式查找
findall = re.findall('火星', a)
print(findall)
if findall:
    print('a 含有“火星”这个字符串')
else:
    print('a 不含有“火星”这个字符串')

# 选择 a 里面的所有小写英文字母
re_findall = re.findall('[a-z]', a)
print(re_findall)

# 检查是否有遗漏知识点
# 1. 使用正则表达式查找所有大写英文字母
uppercase_findall = re.findall('[A-Z]', a)
print('所有大写英文字母:', uppercase_findall)

# 2. 使用正则表达式查找所有中文字符
chinese_findall = re.findall('[\u4e00-\u9fa5]', a)
print('所有中文字符:', chinese_findall)

# 3. 使用正则表达式替换字符串中的某个部分
replaced_a = re.sub('jinxing', '金星', a)
print('替换后的字符串:', replaced_a)

# 4. 使用正则表达式分割字符串
split_a = re.split('\|', a)
print('分割后的字符串列表:', split_a)