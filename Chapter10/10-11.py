#用json格式存储用户输入的数字
import json
list1 = []
file_name = "numbers.json"
while True:
    number = input("请输入喜欢数字")
    if  number == "q":
        break
    try:
        number1 = int(number)
    except ValueError:
        pass
    else:
        list1.append(number1)

with open(file_name,'w') as file_object:
    json.dump(list1,file_object)

#从文件中读取值
file_name1 = 'numbers.json'
with open(file_name1) as file_object:
    number = json.load(file_object)
print(number)




