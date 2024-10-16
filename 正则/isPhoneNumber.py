# 检查是否是手机号格式
from django.contrib.gis.db.backends.postgis.pgraster import chunk


def isPhoneNumber(text):
    if len(text)!=12: #先检查字符串是否够12个字符串
        return False
    for i in range(0,3):
        if not text[i].isdecimal(): # isdecimal()是否自己只包含数字   isdecimal()是‌Python中的一个内置方法，用于检查字符串是否仅包含‌十进制数字字符
            return False
    if text[3] !='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
'''代替下面四个语句'''
message ='Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):# for每次循环都会取自message中的12个字符赋值给chunk
    chunk=message[i:i+12]   #第一次赋值即字符（Call me at 4） 下次迭代就是接下来的字符
    if isPhoneNumber(chunk): #利用isPhoneNumber()函数来判断是否是电话号码格式 如果是就打印出来
        print('Phone number found:'+chunk)
print('Done')




#
# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneNumber('Moshi moshi'))

