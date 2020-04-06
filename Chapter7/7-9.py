#使用while 循环，剔除重复的数据

sandwich_orders = ['fish','pastrami','sugar','pastrami','shrump','pastrami']

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for so in sandwich_orders:
    print(so)