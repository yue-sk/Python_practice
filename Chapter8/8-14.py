#使用任意数量的关键之实参

def make_car(make, size , **source):
    profile = { }
    profile['maker'] = make
    profile['size']  = size

    for key,value in source.items():
        profile[key] = value
    return profile

user_profile = make_car('subaru', 'outback' ,color = 'blue', two_package = 'True')
print(user_profile)
