import matplotlib.pyplot as plt

x_values = list(range(5))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues)

#设置图表标题并给坐标轴上加上标签
plt.title("Cubes", fontsize=24)
plt.xlabel("value", fontsize=24)
plt.ylabel("yvalue", fontsize=24)


plt.axis([0,5,0,100])

plt.show()
