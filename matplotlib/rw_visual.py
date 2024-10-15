import matplotlib.pyplot as plt
from random_walk import RandomWalk
'''导入pyplot 和RandomWalk 类'''
'''创建一个RandomWalk 实例'''
#創建一個RandomWalk 实例 并将其包含的点都绘制出来
rw =RandomWalk()
rw.fill_walk() #将其存储到rw 调用fill_walk
plt.scatter(rw.x_values,rw.y_values,s=15) #将值传递给scatter()
plt.show()