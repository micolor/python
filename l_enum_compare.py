#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
演示Python枚举类的比较操作和排序功能
# Enum 类的枚举是不支持大小运算符的比较
# 使用 IntEnum 类进行枚举，就支持比较功能
# 枚举成员可以通过名字或值来访问
# 枚举成员是单例的，可以使用 is 运算符进行身份比较
"""
from enum import IntEnum


class UserType(IntEnum):
    """用户类型枚举
    
    定义不同类型用户的年龄值
    """
    TEACHER = 98
    STUDENT = 30
    CHILD = 12


if __name__ == "__main__":
    """主函数，演示枚举的比较操作"""
    # 枚举成员实例化
    teacher = UserType.TEACHER
    student = UserType.STUDENT

    # 演示枚举比较操作
    print(f"相等性比较: {teacher == student}, "f"同一枚举成员比较: {teacher == UserType.TEACHER}")
    print(f"身份比较: {teacher is student}, "f"同一枚举成员身份: {teacher is UserType.TEACHER}")

    # 演示枚举成员的访问
    print(f"通过名字访问: {UserType['TEACHER']}")
    print(f"通过值访问: {UserType(98)}")

    # 演示枚举成员的比较操作
    print(f"大小比较: {teacher > student}, {teacher < student}")

    try:
        print("\n按值排序的枚举成员:")
        print('\n'.join(f"  {member.name} = {member.value}" 
                       for member in sorted(UserType)))
    except TypeError as err:
        print(f" 错误: {err}")

    # 枚举成员是单例的，演示 is 运算符
    another_teacher = UserType.TEACHER
    print(f"身份比较: {teacher is another_teacher}")
