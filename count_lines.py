import sys
import os

""" 统计我当前代码一共写了多少行 """


def get_file_name():
    """ 获取文件名"""
    file_list = []
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        # root 正在遍历的目录路径 dirs正在遍历的目录下所有的子目录名称 files 当前文件夹下文件名
        for name in files:
            if os.path.splitext(name)[1] == '.py':
                file_list.append(os.path.join(root, name))
        # for name in dirs:
        #     if os.path.splitext(name)[1] == '.py':
        #         file_list.append(os.path.join(root, name))
    return file_list


def line_count(file_name):
    """
    计算文件行数, 不包括空行
    :param file_name: 文件名
    """
    with open(file_name, 'r', encoding="UTF-8") as f:
        file_context = f.readlines()  # 文件内容
        count = len(file_context)  # 总行数
        n_count = file_context.count('\n')  # 有换行的行数
        true_lins = count - n_count
    return true_lins


if __name__ == "__main__":
    total_line = 0  # 累计行数
    file_list = get_file_name()  # 要遍历的文件列表
    for i in file_list:
        lines = line_count(i)
        print(f"{i}文件有{lines}行")
        total_line += lines
    print(f'我现在一共写了{total_line}代码')
