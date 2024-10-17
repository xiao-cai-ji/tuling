import re

from xlwt.ExcelMagic import ptgEQ

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject3 
@File    ：通配字符.py
@IDE     ：PyCharm 
@Author  ：Flipped
@Date    ：2024/10/17 11:37 
@explain : 文件说明
'''
atRegex=re.compile(r'.at')# . 字符成为通配符 匹配除换行之外的所有的字符
print(atRegex.findall('The cat in the hat sat on the flat mat'))
# 用点-星匹配所有字符 使用的是贪心模式匹配尽可能多的文本
nameRegex=re.compile(r'First Name: (.*) Last Name: (.*)')
mo=nameRegex.search('First Name: AI Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
nongreedyRegex =re.compile(r'<.*?>')#贪心模式 # 匹配一个< 接下来就是任意字符，接下来就是>
mo1=nongreedyRegex.search('<To serve man> for dinner.>')
print(mo1.group())
greedyregex=re.compile(r'<.*>')# 非贪心模式
mo2=greedyregex.search('<To serve man> for dinner.>')
print(mo2.group())

'''用.* 字符匹配换行'''
noNewlineRegex=re.compile('.*')# 在创建时没有传入re.DOTALL 将匹配所字符，知道第一个换行符
print(noNewlineRegex.search('The cat in the hat sat on.\the flat mat').group())

noNewlineRegex=re.compile('.*',re.DOTALL)# 传入了re.DOTALL 将匹配所有字符
print(noNewlineRegex.search('The cat in the.\hat sat on.\the flat mat').group())