import csv

import matplotlib.pyplot as plt

filename='sitka_weather_07-2018_simple.csv'

with open(filename) as f: #将文件名另起一个外号 f
    reader=csv.reader(f)
    herder_row=next(reader) #读取文件的首行

    highs=[]
    for row in reader:
        high=int(row[5])
        highs.append(high)
#print(highs)
plt.style.use('ggplot')
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
fig,ax=plt.subplots()
ax.plot(highs,color='blue',label='high')

plt.title('7月每日最高温-2018',fontweight=24) #图表表题
plt.xlabel('',fontsize=16)# 图表x轴的名称
plt.ylabel('温度（F）',fontsize=16)# 图表x轴的名称
plt.tick_params(axis='both',which='major',labelsize=16) #
plt.show()

'''   for index,column_header in enumerate(herder_row):# enumerate 给定一个数组，给出数据和下标
        print(index,column_header)
'''