""" 练习 38. 操作列表 """

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix it.")

stuff = ten_things.split(' ') # 以空格分隔字符串转为列表
more_stuff = ['Day', 'Night', 'Song',
              'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()  # 弹出列表的最后一个元素
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

    print("There we go: ", stuff)

    print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())  # 弹出列表的最后一个元素
print(" ".join(stuff))  # what? cool!
print('#'.join(stuff[0:5]))  # super stellar!
