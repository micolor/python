# 枚举 Enum
# 重要特性
# - 枚举成员是单例的
# - 枚举成员是不可变的
# - 枚举类不能被实例化
# - 枚举成员不能被重新赋值

# 枚举(Enum)示例
from enum import Enum, unique, auto

# 使用 Enum 创建枚举类
@unique  # 确保枚举成员名称唯一
class Month(Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12

# 自动赋值示例
class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

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

print('\n===== 自动赋值的枚举成员 =====')
for color in Color:
    print(f"名称: {color.name}, 值: {color.value}")

# 枚举比较
print('\n===== 枚举比较 =====')
print(f"Month.Jan == Month.Jan: {Month.Jan == Month.Jan}")
print(f"Month.Jan == Month.Feb: {Month.Jan == Month.Feb}")
print(f"Month.Jan is Month.Jan: {Month.Jan is Month.Jan}")
print(f"Month.Jan is Month.Feb: {Month.Jan is Month.Feb}")

# 枚举的其他方法
print('\n===== 枚举的其他方法 =====')
print(f"列出所有枚举成员：{list(Month)}")
print(f"枚举成员的数量：{len(Month)}")