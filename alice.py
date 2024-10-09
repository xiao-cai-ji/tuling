filename=('E:/pythonProject3/源代码文件/chapter_10/alice.txt')
try:
    with open(filename,encoding='utf-8') as f:#首先读取文件中的内容
        content=f.read()
except FileNotFoundError:
    print(f"Sorry the file {filename} was not found.")
else:
    #计算该文件中大致包含多少个单词
    words=content.split()# 然后利用split 分割内容 是根据空格来分割的
    number_words=len(words)
    print(number_words)
    print(f"There are {number_words} words in this file.") # 然后打印出来
