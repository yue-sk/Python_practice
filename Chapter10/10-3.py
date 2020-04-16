#将用户输入写入到一个文件中
#任何一种IO流，严禁放在循环中。写入文件之前，完整掌握一批数据；
#每次write都会清空文本，用a追加

active = True
filename = 'guest.txt'
lines = []
while active:
   name = input("请输入名字：")
   if name =='quit':
     active = False
   else:
       lines.append(name)

with open(filename,'w') as file_object:
    for line in lines:
       file_object.write(line+'\n')

