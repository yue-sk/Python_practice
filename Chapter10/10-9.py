#失败时一声不吭，pass语句

def file_name(name):
    try:
        with open(name) as file_object:
            contens = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(contens)
names = ["cats.txt", "dogs.txt"]
for name in  names:
    file_name(name)