#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject3 
@File    ：文件读写.py
@IDE     ：PyCharm 
@Author  ：Flipped
@Date    ：2024/10/20 9:32 
@explain : 文件读写
1.调用open() 返回一个File() 对象
2.调用File 对象的read() 或 write() 对象
3.调用File 对象的close() 方法 ，关闭文件
'''
import  os
import shelve
helloFile=open('E:\pythonProject3\pythonProject3\读写文章\hello.txt') # 打开文件 首先要打开文件
helloRead=helloFile.read()
print(helloRead)
Sonnet=open('E:\pythonProject3\pythonProject3\读写文章\sonnet29.txt',encoding='utf-8')
print(Sonnet.readline())


'''写入文件 写模式将覆写源文件
以写模式打开bacont 没有就创建一个，首先创建一个bacont 调用write() ,并向write() 传入字符串‘Hello world’
并传入字符，然后关闭文件
'''
baconFile=open('bacon.txt','w')
print(baconFile.write('Hello World!\n'))
baconFile.close()

baconFile=open('bacon.txt','a')#为了文本添加，不影响源文件，而不是取代刚刚写入的文字，需打开添加模式，向文件中写入，然后关闭
print(baconFile.write('Bacon is not a vegetable.'))
baconFile.close()

baconFile=open('bacon.txt')
content=baconFile.read() # 将读到的文件内容保存到content 然后关闭文件
print(content)
baconFile.close()


'''用shelve 模块保存变量'''
shelfile=shelve.open('mydatabase') # 利用shelve.open()  并传入一个文件名 然后将值返回到一个变量 中 然后对变量中的shelf值进行修改，就像它是一个字典一样
cats=['Zophie','Pooka','Simon'] # 创建 一个cats ,
shelfile['cats']=cats # 将列表保存在shefile 中，
shelfile.close()
'''shalf 值不必用读模式或者写模式打开，因为他们在打开后，既能读又能写'''
shelFile=shelve.open('mydatabase')
print(type(shelFile))
print(shelFile['cats'])
shelFile.close()

''' shelf 值有keys() 和values() 方法 ；返回shelf 中键和值的类似的列表值'''

shelfile1=shelve.open('mydatabase')
print(list(shelfile1.keys()))
print(list(shelfile1.values()))
shelFile.close()
