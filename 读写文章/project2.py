#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject3 
@File    ：project2.py
@IDE     ：PyCharm 
@Author  ：Flipped
@Date    ：2024/10/20 10:28 
@explain : 文件说明
'''
''' 用pprint.pformat() 函数保存变量  函数将放回同样的文本字符，而不是打印它'''
import pprint
import MyCats

cats=[{'name':'Zophine','des':'chubby'},{'name':'Pooka','des':'fluffy'}] # 一个字典的列表 保存在变量cats中，为了让cats中的列表在关闭交互环境后还能使用，利用pprint.pformat 将他返回一个字符串
print(pprint.pformat(cats))
fileobj=open('MyCats.py','w') # 将返回的字符串写到一个.py 的文件中
print(fileobj.write('cats='+pprint.pformat(cats)+'\n'))
fileobj.close()


''' 调用写如的文件 进行    读写 '''
print(MyCats.cats)
print(MyCats.cats[0])
print(MyCats.cats[0]['name'])