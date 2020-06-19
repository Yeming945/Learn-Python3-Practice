# 你进入了一个有两扇门的黑暗房间, 你要进入1号还是2号门
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")
door = input("> ")

if door == '1':
    # 有只大熊在吃芝士蛋糕
    print("There's a giant bear here eating a cheese cake.")
    # 你打算怎么做?
    print("What do you do?")
    # 1. 拿走蛋糕
    print("1. Take the cake.")
    # 2. 对熊尖叫
    print("2. Scream at the bear")

    bear = input("> ")

    if bear == "1":
        # 熊吃掉了你的脸, 干的不错!
        print("The bear eats your face off. Good job!")
    elif bear == '2':
        # 熊吃掉了你的腿, 干的不错!
        print("The bear eats you legs off. Good job!")
    else:
        # 或许选这个更好
        print(f"Well, doing {bear} is probably better.")
        # 熊逃走了
        print("Bear runs away.")


elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")

    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
