""" 练习 23 字符串，字节和字符编码 """

import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)  # 递归函数


def print_line(line, encoding, errors):
    next_lang = line.strip()  # 去除两边的空格
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open('languages.txt', encoding="utf-8")

main(languages, encoding, error)
