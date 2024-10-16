# 检查是否是手机号格式
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
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

#测试