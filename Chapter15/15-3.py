import matplotlib.pyplot as plt
import pygal
from random_walk import RandomWalk


rw = RandomWalk(5000)
rw.fill_walk()

point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values)

plt.show()