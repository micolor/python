# Enum 源码解析
# 1. Enum的基本结构
# Enum 在模块 enum.py 中实现，是Python中实现枚举的核心类
# class Enum(metaclass=EnumMeta):
#     """Generic enumeration.
#     Derive from this class to define new enumerations.
#     """
#     def __new__(cls, value):
#         """Create a new member instance."""
#         obj = object.__new__(cls)
#         obj._value_ = value
#         return obj

# 2. 元类说明
# Enum 使用 EnumMeta 作为元类，这使得 Enum 具有了以下特性：
# - 控制枚举类的创建过程
# - 实现枚举成员的不可变性
# - 提供专门的字典视图
# - 支持迭代和比较操作

# 3. 核心实现细节
# class EnumMeta(type):
#     """Metaclass for Enum"""
#     def __new__(metacls, cls, bases, classdict):
#         """控制枚举类的创建过程"""
#         enum_class = super().__new__(metacls, cls, bases, classdict)
#         enum_class._member_map_ = {}
#         for name, value in classdict.items():
#             if not name.startswith('_'):
#                 enum_class._member_map_[name] = value
#         return enum_class

#     @property
#     def __members__(cls):
#         """Returns a mapping of member name->value.
#         This mapping lists all enum members, including aliases. Note that this
#         is a read-only view of the internal mapping.
#         """
#         return MappingProxyType(cls._member_map_)

#     def __iter__(cls):
#         """支持迭代操作"""
#         return iter(cls._member_map_.values())

#     def __len__(cls):
#         """返回枚举成员的数量"""
#         return len(cls._member_map_)

#     def __getitem__(cls, name):
#         """通过名称获取枚举成员"""
#         return cls._member_map_[name]
