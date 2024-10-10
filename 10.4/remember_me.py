# #把用户输入的名字 保存到json文件中
# # 向用户打招呼
# import json
# username = input('what is your name ?')
#
# filename_json='username.json'
#
# with open(filename_json,'w') as f :
#     json.dump(username,f)
#     print(f'{username} has been saved in',filename_json)


### 重构

import json
def get_stored_username():
    """如果有名字就获取他"""
    file ='usernames.json'  #指出usernames.json 赋值给file
    try:#
        with open (file,'r') as f:
            username =json.load(f) #加载文件赋值给username
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入名字"""
    username=input("Enter your new username: ") #提示用户输入名字
    file='usernames,json'
    with open (file,'w') as f:
        json.dump(username,f) #把username值写到f 中   f->file
    return username


def greet_user():
    """用户打招呼，并指出用户名字"""
    username=get_new_username()
    if username:
        print(f'Welcome to back {username}')
    else:
        username=get_new_username()
        print(f'Welcome to back {username}')
greet_user()