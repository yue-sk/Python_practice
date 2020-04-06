#循环截至的条件，必然是一个点，不可能是一个区域
promt = "How old are you"
promt +="\nEnter 'quit' when you are finished"

while True:
    age = input(promt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("free")
    elif age <13:
        print("$10")
    else:
        print("15")