import  json
number =[2,3,5,7,11,13]
f='number.json'
with open(f,'w') as f:
    json.dump(number,f) #要存什么数据，数据存在哪里