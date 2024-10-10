import  json
file_json='username.json'  #相当于把文件赋名，方便后面的使用
with open(file_json) as f:
    username=json.load(f)
    print(f'Welcom to back,{username}')