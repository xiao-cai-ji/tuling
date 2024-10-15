##散点图样式
import matplotlib.pyplot as plt

x_value=range(1,1001)
y_value=[x**2 for x in x_value]
plt.style.use("seaborn")
plt.rcParams['font.sans-serif']=["Microsoft YaHei"] #中文字体设置

fig,ax=plt.subplots()
ax.scatter(x_value,y_value,c=x_value,cmap=plt.cm.Blues,s=1)# 可以使用RGB 换成（）

# 图表的标题
ax.set_title('Squares')
#X 轴的标题
ax.set_xlabel('值',fontsize=14)
# Y轴标题
ax.set_ylabel('值的平方',fontsize=14)
# 刻度标记的大小
ax.tick_params(axis='both', which='major',labelsize=14)

#坐标轴的取值范围
ax.axis([0,1100,0,1100000]) #前面2 是X  后面是Y
plt.savefig('squares.png',dpi=300)
plt.show()