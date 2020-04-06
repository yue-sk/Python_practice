#遍历字典,查看返回值
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
li = ['jen','sarah']
for l in li:
    if l in favorite_languages.keys():
        print("thank you ")
    else:
        print("invite you")
