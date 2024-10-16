import re
# phoneNumberRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')# 电话号码的正则表达式
# mo =phoneNumberRegex.search('My number is 415-555-4242.')# Regex 对象的search() 方法查找传入的表达式
# print('Phone number found:'+mo.group())
phoneNumberRegex=re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo= phoneNumberRegex.search('My number is (415)555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())# groups()返回多个元组
areaCode,mainNumber=mo.groups()
print(areaCode)
print(mainNumber)
# phoneNumberRegex=re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo= phoneNumberRegex.search('My number is (415)(555-4242).')
# num_first= mo.group(1)
# num_second=mo.group(2)
# print(num_first)
# print(num_second)