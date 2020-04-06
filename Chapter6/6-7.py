#字典中存储列表
people = {
    'Lily':['L','y'],
    'Jerry':['J','y'],
    'Tom':['T','m'],
}

#取字典中的值
print(people['Lily'])

for p,os in people.items():
    print(p)
    for o in os:
        print(o)

for p,os in people.items():
    for o in os:
        print(p+o)