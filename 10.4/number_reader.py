import json
f=('number.json')
with open (f) as f :
    number=json.load(f) # 要读取什么数据
print(number)