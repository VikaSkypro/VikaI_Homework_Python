# Площадь квадрата
import math


def square(a):
    return math.ceil(pow(a, 2))


a = float(input("Введите сторону квадрата: "))
s = square(a)
print("Площадь квадрата = ", s)
