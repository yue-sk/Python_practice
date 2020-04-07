#禁止函数修改列表
#传入函数的列表参数进行修改
#函数中传递的参数为列表

magicans = ['A','B','C']
magic = []

def make_great(magicans,magic):
   magicans1 = magicans[:]
   while magicans1:
       magican = magicans1.pop()
       magic.append(magican + "the Great")


def show_magicians(magic):
    for m in magic:
        print(m)

make_great(magicans,magic)
show_magicians(magic)
show_magicians(magicans)