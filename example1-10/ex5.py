""" 练习 5 更多变量和打印 """

my_name = 'Zed a. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'


print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get exactly right
total = my_age + my_height + my_weight
print(f"If i add {my_age}, {my_height}, and{my_weight} I get {total}.")

""" 
附加练习
1. 修改所有的变量，把前面的 my_ 删掉。要更改所有的变量名，而不只是有 = 的部
分。
2. 试着写一些变量，把英尺（inches）和英镑（pounds）换算成厘米（ centimeters）
和千克（kilograms），别自己直接把自己的数据进去，用 python 的数学运算来换
算。
"""
