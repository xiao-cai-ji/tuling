import json
import pandas as pd
import plotly.express as px
filename='eq_data_1_day_m1.json'
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
fig =px.scatter(
    x=lons,
    y=lats,
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,height=800,
    title='全球地震图'
)
fig.write_html('global_earthquake.html')
fig.show()
# print(msgs[:10])
# print( titles[:10])
# print(lons[:10])
# print(lats[:10])#切片