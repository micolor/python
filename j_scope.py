# 作用域
# 在Python中，作用域决定了变量的可见性和生命周期。主要有四种作用域：
# 1. 局部作用域（Local）：在函数内部定义的变量，只在函数内部可见。
# 2. 嵌套作用域（Enclosing）：在嵌套函数中，外部函数的变量对内部函数可见。
# 3. 全局作用域（Global）：在模块级别定义的变量，整个模块内都可见。
# 4. 内置作用域（Built-in）：Python内置的名字空间，例如len()函数。

def _diamond_vip_name(lv):
    # 局部作用域：lv变量只在这个函数内部可见
    return 'DiamondVIP' + str(lv)

def _gold_vip_name(lv):
    # 局部作用域：lv变量只在这个函数内部可见
    return 'GoldVIP' + str(lv)

def get_vip_level_name(lv):
    # 局部作用域：lv变量只在这个函数内部可见
    if lv == 1:
        return _diamond_vip_name(lv)
    else:
        return _gold_vip_name(lv)

# 调用函数并打印返回值
# 全局作用域：get_vip_level_name函数在整个模块内可见
print(get_vip_level_name(1))