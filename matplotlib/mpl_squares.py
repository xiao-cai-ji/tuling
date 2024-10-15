import  matplotlib.pyplot as plt
import matplotlib
squares = [1, 4, 9, 16, 25]
input_value=[1,2,3,4,5]

# 内置样式
plt.style.use('ggplot')

fig,ax=plt.subplots()
ax.plot(input_value,squares,linewidth=3)
# 图表的标题
ax.set_title('Squares')
#X 轴的标题
ax.set_xlabel('值',fontsize=14)
# Y轴标题
ax.set_ylabel('值的平方',fontsize=14)
# 刻度标记的大小
ax.tick_params(axis='both', labelsize=14)
plt.show()


#内置样式

