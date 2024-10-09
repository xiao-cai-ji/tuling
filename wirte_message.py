#文件写入
flie_name='programming.txt'

with open(flie_name,'w') as file_object:
    file_object.write('Hello world!\n')
    file_object.write('I love you.\n')# .\文件写入换行