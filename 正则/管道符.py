import re
heroRege=re.compile(r'Batman|Tina Fey') #r'Batman|Tina Fey' 正则表达式将匹配'Batman' 或'Tina Fey'
mo1=heroRege.search('Batman and Tina Fey.')
print(mo1.group())
mo2 =heroRege.search('Tina Fey and Batman.')
print(mo2.group())

batRegex =re.compile(r'Bat(man|mobile|copter|bat)') #匹配'Batman'、'Batmobile'、'Batcopter'、'Batbat'、
mo3=batRegex.search('Batmobile lost a wheel')
print(mo3.group())
print(mo3.group(1))

'''用？实现可选匹配'''
BatRegex =re.compile(r'Bat(wo)?man')  # (wo)? 模式wo 是可选的分组 正则表达式匹配的文本中，wo 将出现0 或1 次
mo4=BatRegex.search('The Adverntures of Batman')
mo5=BatRegex.search('The Adverntures of Batwoman')
print(mo4.group())
print(mo5.group())
#前面电话的例子
phoneRegex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo6=phoneRegex.search('My number is 415-555-4242')
mo7=phoneRegex.search('My number is 555-4242')
print(mo6.group())
print(mo7.group())
'''用*号匹配0次或多次'''
number=re.compile(r'Bat(wo)*man')
mo8=number.search('The Adverntures of Batman')#0次
mo9=number.search('The Adverntures of Batwoman')#1次
mo10=number.search('The Adverntures of Batwowowowowowowoman')#多次
print(mo8.group())
print(mo10.group())
'''用+号匹配一次或多次'''
number1=re.compile(r'Bat(wo)+man')# wo 至少要出现1次
mo11=number1.search('The Adventures of Batwoman')
mo12=number.search('The Adverntures of Batwowowowowowowoman')
print(mo12.group())
'''花括号匹配特定次数'''
# （He）{3} 匹配3次；（He）{3,5} 匹配3-5次；（He）{3，} 匹配3次到更多；（He）{，5}匹配0-5次
number3 =re.compile(r'Bat(He){3}')
mo13=number3.search('BatHeHeHe')
print(mo13.group())
mo14=number3.search('He')
print(mo14==None)
'''贪心和非贪心匹配'''
greedyRegex=re.compile(r'(Ha){3,5}')# 贪心匹配
mo15=greedyRegex.search('HaHaHaHaHa')
print(mo15.group())
nongreedyRegex=re.compile(r'(Ha){3,5}?')# 非贪心匹配在}后加？
mo16=nongreedyRegex.search('HaHaHaHaHa')
print(mo16.group())