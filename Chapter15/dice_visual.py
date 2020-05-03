from random import randint
import pygal

class Die():
    def __init__(self,numsides):
        self.numsides = numsides
    
    def roll(self):
        return randint(1,self.numsides)


#创建两个D6的色子
die1 = Die(6)
die2 = Die(6)

#投色子多次，将结果存储于列表中
results = []
for foll_num in range(1000):
    reslut = die1.roll() + die2.roll()
    results.append(reslut)

print(results)

#分析结果
frequencies = []
max_result = die1.numsides + die2.numsides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#可视化结果
hist = pygal.Bar()

hist._title = "Resluts of rolling two Die6 dice 1000 times"
hist.x_labels = ["2",'3','4','5','6','7','8','9','10','11','12']
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('dice_visual.svg')