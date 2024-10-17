#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject3 
@File    ：project.py
@IDE     ：PyCharm 
@Author  ：Flipped
@Date    ：2024/10/17 16:25 
@explain :  电话号码和E-mail 地址提取程序
'''
import re,pyperclip
phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))?             #area code
    (\s|-|\.)?                     # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
)''',re.VERBOSE)#
#TODO Create emaiil regex
emailRegex=re.compile(r'''
    [a-zA-Z0-9._%+-] +
    @
    [a-zA-Z0-9.-] +
    (\.[a-zA-Z]{2,4})
''',re.VERBOSE)
#TODO Find matches in clipboard text
text=str(pyperclip.paste())
matchex=[]
for groups in phoneRegex.findall(text):
    phoneNum='-'.join([groups[1],groups[3],groups[5]])
    if groups[8] !='':
        phoneNum+='x'+groups[8]
    matchex.append(phoneNum)
for groups in emailRegex.findall(text):
    matchex.append(groups[0])

#TODO Copy result to the clipBoard
if len(matchex)>0:
    pyperclip.copy('\n'.join(matchex))
    print('Copied to clipboard')
    print('\n'.join(matchex))
else:
    print('No match')


