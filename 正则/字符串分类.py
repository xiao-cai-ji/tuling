#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject3 
@File    ：字符串分类.py
@IDE     ：PyCharm 
@Author  ：Flipped
@Date    ：2024/10/17 11:10 
@explain : \d:0-9中的任何一个数字
\D：除了0-9 以外的任何一个数字
\w:任何字母、数字、下划线
\W:除了\w 以外的任何字符
\s:空格、制表符或换行符
\S:除\s以外的任何字符
'''
import  re
xmasRegex=re.compile(r'\d+\s\w+')# 匹配有一个或多个数字（\d+） 一个空白字符（\s）  一个或多个字母/数字/下划线（\w+）
print(xmasRegex.findall('12 drummers,11 pipers,10 lords, 9 ladies'))

'''建立自己的字符串'''
consonantRegex=re.compile(r'[^aeiouAEIOU]')# 匹配所有非元音字符
consonantRegex1=re.compile(r'[aeiouAEIOU]')# 匹配所有元音字符，不论大小写 [a-zA-Z0-9] 将匹配所有大小字母、大写字母、数字
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))
print(consonantRegex1.findall('RoboCop eats baby food. BABY FOOD.'))
'''插入字符和美元字符'''
beginsWithHello=re.compile(r'^Hello')# 匹配以Hello 开始的字符串
print(beginsWithHello.search('Hello world!'))
print(beginsWithHello.match('He said hello.')==None)
endsWithNumber=re.compile(r'\d$')#匹配以数字0-9 结束的字符串
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.match('Your number is forty two'))
wholeStringIsNum=re.compile(r'^\d+$')# 匹配从开始到结束都是数字的字符串
print(wholeStringIsNum.search('123456'))
print(wholeStringIsNum.match('123456xy7890'))