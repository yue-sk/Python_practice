#结合函数使用while循环
def make_album(artist, title):
    musician = {"artist":artist,"title":title}
    return musician

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    artist = input("artist:")
    if artist == 'q':
        break

    title = input("title:")
    if title == 'q':
        break

    musican = make_album(artist,title)
    print(musican)