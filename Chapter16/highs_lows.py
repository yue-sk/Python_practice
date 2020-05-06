import csv
from matplotlib import pyplot as plt 
from datetime import datetime

filename = "Chapter16\world_fires_1_day.csv"

#输入文件头
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
   #print(header_row)
   #提取并读取数据
    dates,latitude,longtitude = [],[],[]
    for row in reader:
        try:
             current_date = datetime.strptime(row[5],"%Y-%m-%d")
             lat =int(float(row[0]))
             lon = float(row[1])
        except ValueError:
            print(current_date,'missing data')    
        else:
            dates.append(current_date)
            latitude.append(lat)
            longtitude.append(lon)
#print(latitude)
#print(current_date)
print(longtitude)
  
#根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,latitude,c='red')
plt.plot(dates,longtitude,c='blue')
plt.fill_between(dates,latitude,longtitude,facecolor='blue',alpha=0.1)

#设置图形的格式
plt.title("Daily high temperaturel,July 2018",fontsize = 24)
plt.xlabel('',fontsize=16)
plt.ylabel("Temperature",fontsize = 16)
fig.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize = 16)

plt.show()
    

# #打印文件头以及位置
# for index , column_header in enumerate(header_row):
#     print(index, column_header)

