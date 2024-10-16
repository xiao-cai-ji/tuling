from plotly.graph_objs import Bar,Layout
from plotly import offline
from die import Die
import pygal
'''创建一个骰子类'''
die=Die()

#投几次骰子，并将结果存储在一个列表中
results=[]

#随机数
for roll_num in range(1000):
    result=die.roll()
    results.append(result)

# 统计没中数据出现的个数
frequencies=[] # 建立一个空的列表
for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)
#print(frequencies)
x_value=list(range(1,die.num_sides+1))
data=[Bar(x=x_value,y=frequencies)]
x_axis_config={'title':'结果'}
y_axis_config={'title':'结果的频率'}
my_layout=Layout(title='掷一次D6 1000次的结果',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='D6.html')