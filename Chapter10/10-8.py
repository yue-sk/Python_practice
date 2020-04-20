#文件获取失败提示
# file_name1 = "dogs.txt"
#
# try:
#     with open(file_name1) as file_object:
#         contens = file_object.read()
# except FileNotFoundError:
#     print("sorry,not find file")
# else:
#     contens = file_object.read()

file_name = "cats.txt"

try:
    with open(file_name) as file_object:
        contens = file_object.read()
except FileNotFoundError:
    print("sorry,not find file")
else:
    print(contens)