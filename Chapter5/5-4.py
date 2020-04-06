#version1
alien_color = ["green","yellow","red"]
for c in alien_color:
    if c =="green":
        print("get 5 points")
    if c !="green":
        print("get 10 points")

#version2
alien_color = ["green","yellow","red"]
for c in alien_color:
    if c =="green":
        print("get 5 points")
    else:
        print("get 10 points")