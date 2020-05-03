from random import choice
import matplotlib.pyplot as plt 

class RandomWalk():
    """初始化随机漫步的属性"""
    def __init__(self,num_points=500):
        self.num_points = num_points

    #所有的随机漫步最初都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """计算随机漫步所包含的点"""
        while len(self.x_values)  < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step ==0 and y_step ==0:
                continue
            
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

        

    
    def get_step(self):
        """获取随机步长"""
        direction = choice([1,-1])
        distance = choice([1,2,3,4,5,6,7,8])
        step = direction * distance
        
        return step

rw = RandomWalk()
rw.fill_walk()
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values)

plt.show()
    

  
