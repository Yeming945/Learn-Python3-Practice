""" 练习 12 提示用户 """

age = input("How odl are you?")
height = input("How tall are you?")
weight = input("How much do you weight?")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

"""
附加练习
1. 在 Terminal 里输入 pydoc input ，看看它会说什么。如果你用的是 Windows， 输
入 python3.6 -m pydoc input 。
2. 输入 q ，退出 pydoc 。
3. 到网上查查 pydoc 命令的作用。
4. 用 pydoc 读一读关于 open ， file ， os ，和 sys 的内容；浏览一遍即可，把有
意思的东西记下来。
"""
""" 为什么我不能用 print("How old are you?", input()) ？ 你能，只不过 input() 的结果不会被
保存到一个变量里，它会以一种奇怪的方式运行。你可以试试，然后试着打印你输入的东西，看
看你能不能搞明白为什么它无法运行。 """
# 先运行input函数, 把返回值str放入print里打印
print("How old are you?", input())
