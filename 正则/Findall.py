#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject3 
@File    ：Findall.py
@IDE     ：PyCharm 
@Author  ：Flipped
@Date    ：2024/10/17 10:51 
@explain : search() 返回一个Match 对象； findall返回一组字符串
如果在正则表达式中有分组，findall 将返回一个元组的列表
'''
import re
number=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')# 没有分组
mo=number.search('Call:415-555-0000 Work:212-555-0000')
print(number.findall('Call:415-555-0000 Work:212-555-0000'))
print(mo.group())
phoneNumber=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')# 有分组
print(phoneNumber.findall('Call:415-555-0000 Work:212-555-0000')) #返回[('415', '555', '0000'), ('212', '555', '0000')]