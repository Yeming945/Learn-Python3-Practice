""" 练习 17. 更多文件更多文件 """

from sys import argv
from os.path import exists

script, from_file, to_file = argv
# 复制文件的内容到另一个文件
print(f"Copying from {from_file} to {to_file}")

# we cloud do these two on one line, how?
in_file = open(from_file, encoding='UTF-8')
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")

input()

out_file = open(to_file, 'w', encoding='UTF-8')
out_file.write(indata)

print("Alright, all done.")
out_file.close()
in_file.close()
