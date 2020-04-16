#读取文件并打印文件
#全部读取
with open('learning_python.txt') as file_object:
    context = file_object.read()
    print("全部读取")
    print(context)

#逐行读取
with open('learning_python.txt') as file_object:
    for line in  file_object:
        print("逐行读取")
        print(line.rstrip())

#创建一个包含文件各行内容的列表
with open ('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print("包含文件的列表")
    print(line.rstrip())