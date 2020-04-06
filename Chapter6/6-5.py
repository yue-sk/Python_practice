rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for k,v in rivers.items():
    print("The "+ k +"runs throgh "+"Egypt")

for k in rivers.keys():
    print(k)

for v in rivers.values():
    print(v)