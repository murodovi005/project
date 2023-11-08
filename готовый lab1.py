import math


def task1():
    print('Задание 1')
    # Значение х у z
    x = float(input("введи x: "))
    y = float(input("введи y: "))
    z = float(input("введи z: "))

    # Вычисление а
    a_up = (x ** 0.5) - (abs(y ** 0.25))
    a_down = x - math.log2(y)
    a = a_up / a_down

    # Вычисление b
    b_1 = math.tan((x - 1) ** 0.5)
    b_2 = (abs(z)) ** 1 / 3
    b_3 = (y) ** 1 / 6
    b = b_1 - b_2 - b_3 + x
    print("a = {0:.4f} b = {1:.4f}".format(a, b))

task1()


def task2():
    print('Задание 2')

    a = float(input("введи a: "))
    b = float(input("введи b: "))
    c = float(input("введи c: "))
    x = float(input("введи x: "))

    # Числительные дроби
    a_11 = (c * x) ** 0.5
    # Знаменатели дроби
    a_12 = b * x + a
    # Дробь
    a_1 = a_11 / a_12
    a_2 = x ** b

    a = a_2 + a_1

    print("Вычисляем f(x) =", a)

task2()

