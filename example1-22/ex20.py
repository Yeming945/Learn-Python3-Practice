""" 练习 20 函数和文件 """

from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


# 文件指针归零
def rewind(f):
    f.seek(0)  # 改变指针的位置, 从位置0开始读取


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("First let's print the whole file:\n")  # 打印整个文件

print_all(current_file)  # 把文件对象传给print_all

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines: ")

current_line = 1
print_a_line(current_line, current_file)
print(current_file.tell())  # 返回文件读写指针当前所处的位置

current_line += 1
print_a_line(current_line, current_file)
print(current_file.tell())  # 返回文件读写指针当前所处的位置

current_line += 1
print_a_line(current_line, current_file)
print(current_file.tell())  # 返回文件读写指针当前所处的位置
