import math


def square(side):
    return math.ceil(side * side)


s_square = float(input("Введите длину стороны квадрата: "))
print(f"Площадь квадрата: {square(s_square)}")
