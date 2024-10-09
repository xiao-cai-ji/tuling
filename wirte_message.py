#文件写入
flie_name='programming.txt'

with open(flie_name,'w') as file_object:
    file_object.write('Hello world!')