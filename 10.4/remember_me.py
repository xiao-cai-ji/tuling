#把用户输入的名字 保存到json文件中
# 向用户打招呼
import json
username = input('what is your name ?')

filename_json='username.json'

with open(filename_json,'w') as f :
    json.dump(username,f)
    print(f'{username} has been saved in',filename_json)