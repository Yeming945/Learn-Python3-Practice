""" 练习 13 参数，解包，变量 """

from sys import argv
# read the WYSS section for how to run this
# 在命令行运行时传入3个参数
script, first, second, third = argv

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

"""
python ex13.py 1 2 3
The script is called:  ex13.py
Your first variable is:  1
Your second variable is:  2
Your third variable is:  3 
"""
