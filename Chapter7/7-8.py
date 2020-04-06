#判断列表是否为空，将列表中的内容转移到另一个列表

sandwich_orders = ['fish','sugar','shrump']
finished_sandwiches = []

while sandwich_orders:
    sr = sandwich_orders.pop()
    finished_sandwiches.append(sr)

for sf in finished_sandwiches:
     print(sf)
