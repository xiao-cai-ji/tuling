from openpyxl.styles.builtins import percent

file_path='E:/pythonProject3/源代码文件/chapter_10/pi_million_digits.txt'
with open(file_path) as file_object:
    lins=file_object.readlines()
pi_string=''
for line in lins:
    pi_string+=line.rstrip()
birthday =input('Enter your birthday: ')
if birthday in pi_string:
    print('your birthday is', birthday)
else:
    print('Sorry')
# print(f'{pi_string[:52]}...')
# print(len(pi_string))
    # for line in file_object:
    #     print(line.rstrip())#rstrip剔除换行
#     content = file_object.read()
# print(content)

