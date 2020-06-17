import sys
import os

""" 统计我当前代码一共写了多少行 """


def get_file_name():
    """ 获取文件名"""
    # 待处理的文件列表
    file_list = []
    path = os.getcwd()
    com_path = path + "\\example1-22\\"
    f_list = os.listdir(path + '\\example1-22')
    for i in f_list:
        file_list.append(com_path + i)
    return file_list


def line_count(file_name):
    """
    计算文件行数
    :param file_name: 文件名
    """
    with open(file_name, 'r', encoding="UTF-8") as f:
        count = len(f.readlines())
    return count


if __name__ == "__main__":
    total_line = 0
    file_list = get_file_name()
    for i in file_list:
        lines = line_count(i)
        print(f"{i}文件有{lines}行")
        total_line += lines
    print(f'我现在一共写了{total_line}代码')
