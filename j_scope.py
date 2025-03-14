# 作用域
def _diamond_vip_name(lv):
    return 'DiamondVIP' + str(lv)

def _gold_vip_name(lv):
    return 'GoldVIP' + str(lv)

def get_vip_level_name(lv):
    if lv == 1:
        return _diamond_vip_name(lv)
    else:
        return _gold_vip_name(lv)

# 调用函数并打印返回值
print(get_vip_level_name(1))