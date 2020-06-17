""" 练习 21 函数可以返回一些东西 """


def add(a, b):
    """ 加法 """
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    """ 减法 """
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    """ 乘法 """
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    """ 除法 """
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")
