#导入字典库
from collections import OrderedDict

order_dict = OrderedDict()
order_dict['1'] = 'A'
order_dict['2'] = 'B'
order_dict['3'] = 'C'

for key,value in order_dict.items():
    print(key + "相对于" + value)


