#返回字典
def make_album(artist, title):
    musician = {"artist":artist,"title":title}
    return musician

music=make_album("A","B")
print(music)

#可选形参
def make_album(artist, title, num=' '):
    musician = {"artist":artist,"title":title}
    if num:
        musician['num'] = num
    return musician

music=make_album("B","C")
print(music)
music=make_album("B","C","6")
print(music)