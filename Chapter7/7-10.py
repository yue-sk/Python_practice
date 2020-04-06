#用户输入填充字典
resp = { }

active = True
while active:
    mes1 = input("Are you ready")
    mes2 = input("where are you would you like to go")
    resp[mes1] = mes2
    mes3 = input("yes or no")
    if mes3 =='no':
        active = False

for m1,m2 in resp.items():
    print(m1 + m2)
