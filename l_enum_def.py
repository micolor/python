# 自定义枚举

from enum import Enum, unique

# 使用 Enum 创建一个简单的枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# @unique 装饰器可以帮助我们检查保证没有重复值
@unique
class Month(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September'
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'

# 枚举类的使用示例
if __name__ == '__main__':
    # 访问枚举成员
    print(Month.Jan, '----------', Month.Jan.name, '----------', Month.Jan.value)
    
    # 遍历枚举成员
    for name, member in Month.__members__.items():
        print(name, '----------', member, '----------', member.value)
    
    # 枚举成员的比较
    print(Month.Jan == Month.Jan)  # True
    print(Month.Jan == Month.Feb)  # False
    
    # 枚举成员的类型和属性
    print(type(Month.Jan))  # <enum 'Month'>
    print(isinstance(Month.Jan, Month))  # True