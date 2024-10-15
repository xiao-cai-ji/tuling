import matplotlib.pyplot as plt
from random_walk import RandomWalk
'''导入pyplot 和RandomWalk 类'''
'''创建一个RandomWalk 实例'''
#創建一個RandomWalk 实例 并将其包含的点都绘制出来



while True:
    rw = RandomWalk()
    rw.fill_walk()  # 将其存储到rw 调用fill_walk
    ''' 给点着色'''
    point_number=list(range(rw.num_points)) #生成一个数字列表，包含的数字个数与漫步的点数相同
    plt.scatter(rw.x_values,rw.y_values,c=point_number,cmap=plt.cm.Blues,
                edgecolors='none',s=15)  # 指定使用颜色为Blues, 传递实参edgecolors =none 删除每个点周围的轮廓
    '''突出起点和终点'''
    plt.scatter(0,0,c='green',edgecolors='none',s=100) # 使用绿色绘制第一个点 s=100 使其它比其他点都要大
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    '''隐藏坐标轴'''
    plt.axes().get_xaxis().set_visible(True) #是可以看见坐标轴
    plt.axes().get_yaxis().set_visible(False)# 看不见坐标轴
#    plt.scatter(rw.x_values, rw.y_values, s=5)  # 将值传递给scatter()
    plt.show()

    keep_running =input('Do you want to continue (y/n) :')
    if keep_running=='n':
        break