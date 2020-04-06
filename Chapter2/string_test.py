#2-3:字符串拼接
name = input("请输入用户姓名")
#message =" Hello "+ name+",Woulid you like to learn some Python today"
#print(message)
print("Hello "+ name + ",Woulid you like to learn some Python today")

#2-4:字符串大小写转换以及字符串首字符大写
name = input("请输入用户姓名")
name = name.lower()
print(name)
name = name.upper()
print(name)
name = name.title()
print(name)

#""和''都可以标识字符串
print('Albert once said,"A person who never made a mistake never tried anything new"')

#字符串拼接
name = "Albert"
message = '"A person who never made a mistake never tried anything new"'
print(name+" once said."+message)

#字符串中的空白
name = "\n\t\n\t yueyue \n\t\n\t"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())