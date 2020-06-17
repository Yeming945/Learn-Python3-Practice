""" 练习 15 阅读文件
'r'     open for reading (default) 只读方式打开
'w'     open for writing, truncating the file first 写入方式打开 清空文件
'x'     create a new file and open it for writing 创建一个文件并写入
'a'     open for writing, appending to the end of the file if it exists 写入文件, 添加到文件的末尾
'b'     binary mode 二进制模式
't'     text mode (default)
'+'     open a disk file for updating (reading and writing) 增强模式
'U'     universal newline mode (deprecated) "   
"""
from sys import argv

script, filename = argv  # 运行时输入文件名

txt = open(filename)  # 打开文件

print(f"Here's your file {filename}:")
print(txt.read())  # 读取文件

print("Type the filename again:")

file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
