#字典的遍历
dict = {
    'str': 'A series of characters.',
    'c': 'A note in a program that the Python interpreter ignores.',
    'li': 'A collection of items in a particular order.',
    'lo': 'Work through a collection of items, one at a time.',
    'di': "A collection of key-value pairs.",
    }
for  k,v in dict.items():
    print(k)
    print(v)

for k in dict.keys():
    print(k)

for v in dict.values():
    print(v)