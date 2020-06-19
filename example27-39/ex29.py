""" 练习 29 if 语句 """

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs")

""" 附加练习
在附加练习中，试着猜猜 if 语句是什么以及它是干什么的。在继续进行下个练习之前，试着用
自己的话回答以下这些问题，
1. 你认为 if 对它下面的代码起什么作用？ 条件判断, 为True时执行下面的语句
2. 为什么 if 下面的代码要缩进 4 个空格？ Ptyhon用空格作为代码块缩进
3. 如果没有缩进会发生什么？ 会出现语法错误
4. 你能从练习 27 里面把一些布尔表达式放进 if 语句吗？试试看。
5. 如果你改变 people，cats 和 dogs 的初始值会发生什么？ 
"""
