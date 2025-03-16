# 条件语句
# ==================

# 1. 基础if-else语句示例
# 判断成绩是否及格的简单示例
results = 59
if results >= 60:
    print('及格')  # 当results >= 60时输出
else:
    print('不及格')  # 当results < 60时输出

# 2. Python真值判断
# Python中任何非0和非空值都视为True
print("\n真值判断示例：")
num = 6 
if num:
    print('num = 6 的结果：True')  # 6是非0值，所以为True

if 0:
    print('0 的结果：True')
else:
    print('0 的结果：False')  # 0为False

if '':
    print('空字符串的结果：True')
else:
    print('空字符串的结果：False')  # 空字符串为False

# 3. if-elif-else多分支结构
# 成绩等级判断示例
print("\n成绩等级判断：")
results = 89
if results > 90:
    print('优秀')  # 90分以上
elif results > 80:
    print('良好')  # 80-90分
elif results > 60:
    print('及格')  # 60-80分
else:
    print('不及格')  # 60分以下

# 4. 复合条件判断
print("\n复合条件判断：")
java = 86
python = 68

# 使用and运算符（两个条件都必须为True）
if java > 80 and python > 80:
    print('两科都优秀')
else:
    print('至少一科不够优秀')

# 使用or运算符（任意一个条件为True即可）
if (java >= 80 and java < 90) or (python >= 80 and python < 90):
    print('至少一科成绩良好')

# 5. if嵌套示例
print("\n嵌套条件判断：")
if java > 80:
    if python > 80:
        print('两科都超过80分')
    else:
        print('只有Java超过80分')
else:
    print('Java没有超过80分')

