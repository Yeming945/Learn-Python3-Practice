""" 练习 6 字符串和文本 """

types_of_people = 10
x = f"There are {types_of_people} types of people." # 有10种类型的人

binary = "binary"
do_not  = "don't"
y = f"Those who know {binary} and those who {do_not}." # 有些人知道二进制和不知道的
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)

""" 
附加练习
1. 复习一遍这个程序，并在每一行上面写上注释来解释它。
2. 找到所有把字符串放在字符串里面的地方，一共有 4 处。
3. 你确定有 4 处吗？你怎么知道？也许我爱撒谎呢。
4. 解释一下为什么把 w 和 e 两个字符串用 + 连起来能够弄成一个更长的字符串。 +号可以连接字符串
"""