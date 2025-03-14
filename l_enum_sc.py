# Enum 源码解析
# 1. Enum的基本结构
# Enum 在模块 enum.py 中实现，是Python中实现枚举的核心类
# class Enum(metaclass=EnumMeta):
#     """Generic enumeration.
#     Derive from this class to define new enumerations.
#     """

# 2. 元类说明
# Enum 使用 EnumMeta 作为元类，这使得 Enum 具有了以下特性：
# - 控制枚举类的创建过程
# - 实现枚举成员的不可变性
# - 提供专门的字典视图

# 3. 核心实现细节
# class EnumMeta(type):
#     """Metaclass for Enum"""
#     @property
#     def __members__(cls):
#         """Returns a mapping of member name->value.
#         This mapping lists all enum members, including aliases. Note that this
#         is a read-only view of the internal mapping.
#         """
#         return MappingProxyType(cls._member_map_)
