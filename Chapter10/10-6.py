#用户输入，做加法运算，类型转换抛异常
#else代码块中，

try:
   a = int(input("请输入a:"))
   b = int(input("请输入b:"))
except ValueError:
    print("请输入数字")

else:
   sum = a + b
   print("和为:" + str(a) + '+' + str(b) + '=' + str(sum))

