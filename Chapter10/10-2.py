#查找文件中的字符，并将该字符进行替换
#python 中的replace函数

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
    print(line)
    #print(len(line))

    if 'Python' in line:
        line = line.replace('Python','C')
        print(line)