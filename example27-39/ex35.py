""" 练习 35 分支和函数 """

from sys import exit


def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)  # 字符串转数字

    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)

    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")  # 这里有只熊
    print("The bear has a bunch of honey.")  # 熊有一堆蜂蜜
    print("The fat bear is in front of another door.")  # 大熊在另一扇门前
    print("How are you going to move the bear?")  # 你要怎么让熊走开
    bear_moved = False

    while True:
        choice = input("enter 'take honey' or taunt bear' or 'open door':> ")
        if choice == "take honey":
            dead("The bear looks at you then slaps your face")  # 熊看到你然后拍了你的脸

        elif choice == "taunt bear" and not bear_moved:  # 嘲讽熊
            print("The bear has moved from the door.")  # 熊已经移到另一扇门边了
            print("You can go through it now.")
            bear_moved = True

        # 第二次输入taunt bear才会执行到这
        elif choice == 'taunt bear' and bear_moved:
            dead("The bear gets pissed off and chews you leg.")  # 熊生气了, 吃了你的腿

        elif choice == 'open door' and bear_moved:
            gold_room()

        else:
            print("I got no idea what that means.")


def cthulhu_room():
    """ 克苏鲁房间 """
    print("Here you see the great evil Cthulhu.")
    print("he, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("enter 'flee' or 'head'>: ")

    if "flee" in choice:
        start()

    elif "head" in choice:
        dead("Well that was tasty!")

    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in dark room.")  # 你在一个黑暗的房间里
    print("There is a door to your right and left.")  # 你的左右两边各有一扇门
    print("Which one do you take?")  # 你选择哪一个

    choice = input("enter left or right:> ")

    if choice == 'left':
        bear_room()

    elif choice == "right":
        cthulhu_room()

    else:
        # 你在房间里跌倒了, 最后你饿死了
        dead("You stumble around the roo until you starve.")


start()
