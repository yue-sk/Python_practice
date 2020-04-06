#创建列表
name = ["lx","lr","yy","lc","lj"]
for i in name:
       print(i + " invaite you eat dinner with me ")

#列表删除与添加
name = ["lx","lr","yy","lc","lj"]
xx = "yy"
name.remove("yy")
for i in name:
       print(i + " invaite you eat dinner with me ")
print(xx+"can not to eat dinner")

#列表元素的替换
name = ["lx","lr","yy","lc","lj"]
x = "yy"
n=0
for i  in  name:
       if(i==x):
              print(n)
              break
       else:
             n+=1
name[n] = "gg"
print(name)


#遍历查找位置

for i in name:
       print(i + " invaite you eat dinner with me ")

#列表元素添加
name = ["lx","lr","yy","lc","lj"]
name.insert(0,"jf")
name.insert(2,"hd")
name.append("zh")
print(name)
for i in name:
       print(i + " invaite you eat dinner with me ")

#列表缩减
print("sorry,i can just invite two people eat dinner with me")
name = ["lx","lr","yy","lc","lj"]
while(len(name)!=2):
   x = name.pop()
   print(x+" sorry,next invite you ")




