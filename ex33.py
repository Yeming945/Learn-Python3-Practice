""" 练习 34 获取列表元素 """

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")
for num in numbers:
    print(num)

""" 附加练习
1. 把这个 while-loop 转换成一个你可以调用的函数，然后用一个变量替代 i < 6 里面的
6。
2. 用这个函数重新写一下这个脚本，试试不同的数值。
3. 再增加一个变量给这个函数的参数，然后改变第 8 行的 +1，让它增加的值与之前不
同。
4. 用这个函数重新写这个脚本，看看会产生什么样的效果。
5. 用 for-loop 和 range 写这个脚本。你还需要中间的增加值吗？如果不去掉这个增加
值会发生什么？
 """

# 练习1


def while_loop(num):
    i = 0
    numbers = []
    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for x in numbers:
        print(x)


while_loop(10)
