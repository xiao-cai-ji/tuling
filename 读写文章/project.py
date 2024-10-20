#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject3 
@File    ：project.py
@IDE     ：PyCharm 
@Author  ：Flipped
@Date    ：2024/10/20 8:54 
@explain : 读写文章
'''
import os
print(os.getcwd()) #获得当前工作路径
# (os.makedirs('E:\\pythonProject3\\pythonProject3\waffles'))# 创建文件夹

'''os.path :   os.path.abspath (将返回参数的绝对路径的字符串，将相对路径转换为绝对路径的简便方法)；os.path.isabs(path):如果参数是一个绝对路径，就返回True 如果参数是一个相对路径，就返回False'''
print(os.path.abspath('.')) #调用时返回当前文件夹 也就是绝对路径
print(os.path.abspath('.\\Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))#如果是绝对路径则返回True

'''查看文件大小和文件夹内容   os.path.getsize(path) 返回path参数中文件的字节数；os.listdir(path) 返回文件名字符串的列表 包含path参数中的每个文件'''
print(os.path.getsize('E:\\pythonProject3\\pythonProject3\\正则\\Findall.py'))
print(os.listdir('E:\\pythonProject3\\pythonProject3\\正则\\'))

totalSize=0
for filename in os.listdir('E:\\pythonProject3\\pythonProject3\\正则\\'): # 遍历每一个文件夹 使用join() 来连接文件名和当前文件名（os.path.join使用来拼接路径）
    totalSize=totalSize+os.path.getsize(os.path.join('E:\\pythonProject3\\pythonProject3\\正则\\',filename))
print(totalSize)

'''检查路径的有效性
文件夹存在 os.path.exists(path)  返回True False
如果Path 参数存在，并且是一个文件，调用os.path.isfile(path) 返回True False
如果Path 并且是一个文件夹 调用os.path.isdir(path) 返回True False
利用os.path.exists() 函数 可以确定DVD 或者闪存盘当前是否连接到计算机上，
'''
print(os.path.exists(os.path.abspath('.\\Scripts')))
print(os.path.exists('c:\\Windows\\System32'))
print(os.path.isfile('c:\\Windows\\System32'))
print(os.path.isdir('c:\\Windows\\System32'))