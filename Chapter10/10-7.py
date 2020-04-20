#else代码块：
#依赖于try代码块成功执行的代码都应放到else代码块中

sum = 0
while True:
   first_number = input("\nfirst_number")
   if first_number == "q":
       break
   second_number = input("\nsecond_number")
   try:
       sum = int(first_number) + int(second_number)
   except ValueError:
       print("请输入数字")
   else:
        print(sum)




