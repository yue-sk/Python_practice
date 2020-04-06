#字典中存列表
favorite_site={
    'znn': ['chengdu', 'shanghai', 'hangzhou'],
    'yl': ['chengdu', 'huang montains'],
    'other': ['xian', 'xinjiang', 'nanji']
}

for name, places in favorite_site.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())