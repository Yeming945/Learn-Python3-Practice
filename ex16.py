""" 练习 16. 读写文件写文件 
• close - 关闭文件，就像编辑器中的 “文件->另存为”一样。 
• read - 读取文件内容。你可以把读取结果赋给一个变量。
• readline - 只读取文本文件的一行内容。
• truncate - 清空文件。清空的时候要当心。
• write('stuff') - 给文件写入一些“东西”。 
• seek(0) - 把读/写的位置移到文件最开头。
"""

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.") # 我们要删除这个文件
print("If you don't want that, hit CTRL-C (^C).") # 如果你不想这样做, 请按CTRL-C
print("If you do want that, hit RETURN.") # 如果你想要删除, 点击RETURN

input('?')

print("Opening the file...") # 正在打开文件
target = open(filename, 'w', encoding='UTF-8') 

print("Truncating the file. Goodbye!")
target.truncate() # 清空文件

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() # 关闭文件