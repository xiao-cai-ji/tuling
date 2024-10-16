import json
import pandas as pd
import plotly.express as px
filename='eq_data_30_day_m1.json'
with open(filename,'r') as f:
    all_eq_date=json.load(f)
    all_eq_dicts=all_eq_date['features']
msgs,titles,lons,lats=[],[],[],[],
for eq_dicts in all_eq_dicts:
    msg=eq_dicts['properties']['mag']
    title=eq_dicts['properties']['title']
    lon=eq_dicts['geometry']['coordinates'][0]
    lat= eq_dicts['geometry']['coordinates'][1]
    msgs.append(msg)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
data=pd.DataFrame(
    data=zip(lons,lats,titles,msgs),columns=('经度','纬度','位置','震级',)
)
data.head()
fig =px.scatter(
    data,
    x='经度',
    y='纬度',
    #lab
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,height=800,
    title='全球地震图',
    size='震级',
    size_max=10,
    color='震级',
    color_continuous_scale='viridis',

)
fig.write_html('global_earthquake.html')
fig.show()
# print(msgs[:10])
# print( titles[:10])
# print(lons[:10])
# print(lats[:10])#切片
