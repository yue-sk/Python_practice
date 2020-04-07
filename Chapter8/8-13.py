#使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = { }
    profile['first_name'] = first
    profile['last_name'] = last
    print(profile)
    #遍历在user_info 中的键值对，并将每一个都加入到字典profile中。
    for key , value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('a', 'b',field = 'physics')
print(user_profile)