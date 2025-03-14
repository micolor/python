# 枚举 Enum
# 重要特性
# - 枚举成员是单例的
# - 枚举成员是不可变的
# - 枚举类不能被实例化
# - 枚举成员不能被重新赋值

# 枚举(Enum)示例
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 输出所有枚举成员
print('===== 遍历枚举成员 =====')
for name, member in Month.__members__.items():
    print(f"名称: {name}, 成员: {member}, 值: {member.value}")

print('\n===== 枚举的使用方式 =====')
# 直接引用枚举成员
print(f"获取枚举成员：{Month.Jan}")
# 通过值获取枚举成员
print(f"通过值获取枚举：{Month(1)}")
# 获取名称和值
print(f"获取枚举名称：{Month.Jan.name}")
print(f"获取枚举值：{Month.Jan.value}")