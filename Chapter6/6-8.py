#列表中存字典

pets = []

pet = {
    'type': 'fish',
    'name': 'john',
    'owner': 'guido',
}
pets.append(pet)

pet = {
    'type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
}
pets.append(pet)

pet = {
    'type': 'dog',
    'name': 'peso',
    'owner': 'eric',
}
pets.append(pet)

print(pets)

for p in pets:
    print(p)