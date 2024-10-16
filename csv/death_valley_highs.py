import csv
from datetime import datetime

from matplotlib import pyplot as plt

from alice import filename

filename='death_valley_2018_simple.csv'
with open(filename) as f: #将文件名另起一个外号 f
    reader=csv.reader(f)
    herder_row=next(reader) #读取文件的首行

    dates,highs,lows=[],[],[] #定义两个数组，一个存储日期，一个存数值
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d') # 日期字符串 转换
        try:
            high=int(row[5])
            low=int(row[6])
        except ValueError:
            print('Missing Date')
        else:
            lows.append(low)
            highs.append(high)
            dates.append(current_date)
#print(highs)
plt.style.use('ggplot')
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
fig,ax=plt.subplots()
ax.plot(dates,lows,color='blue',alpha=0.5)
ax.plot(dates,highs,color='red',alpha=0.5)
ax.fill_between(dates,lows,highs,facecolor='blue',alpha=0.1)

plt.title('2018年每日最高最低气温\n死亡谷，CA',fontweight=24) #图表表题
plt.xlabel('',fontsize=16)# 图表x轴的名称
fig.autofmt_xdate() #倾斜的日期
plt.ylabel('温度（F）',fontsize=16)# 图表x轴的名称
plt.tick_params(axis='both',which='major',labelsize=16) #
plt.show()
