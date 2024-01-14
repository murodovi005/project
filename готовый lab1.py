import math
def task1():
    print("Задание №1")
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
    # Конечный ответ
    print("a = {0:.4f} b = {1:.4f}".format(a, b))
#task1()
def task2():
    print("Задание №2")
    a = 5
    b = 2
    c =-5
    x = float(input("введи x: "))
    # Числительные дроби
    a_11 = (c * x) ** 0.5
    # Знаменатели дроби
    a_12 = b * x + a
    # Дробь
    a_1 = a_11 / a_12
    a_2 = x ** b
    # Конечный ответ
    a = a_2 + a_1
    print("Вычисляем f(x) = {0:.4f} ".format(a))
#task2()
def task3():
    print("Задание №3")
    x = float(input("введи x: "))
    # Заданная формула
    ab_1 = (math.cos(x) ** 2 * (math.sin(1 / (x ** 2))))
    # Конечный ответ
    print("Вычисляем f(x) = {0:.4f} ".format(ab_1))
#task3()
def task4():
    print("Задание №4")
    k = float(input("введи сторону К: "))
    alfha = float(input("введи угол альфу: "))
    beta = float(input("введи угол бетту: "))
    # Чтобы найти 3ий угол нужно из 180 минусовать сумма 2 углов
    gamma = 180 - (alfha + beta)
    # Числитель дроби
    S1 = 1 / 2 * k ** 2
    # Знаменатель дроби
    S2 = math.sin(alfha) * math.sin(beta) / math.sin(gamma)
    # Формула такая: S = (a^2/2)*((sinA * sinB)/sinY)
    S = S1 * S2
    # Конечный ответ
    print("S = {0:.4f} ".format(S))
#task4()
def task5():
    print("Задание №5")
    v1 = float(input("Объёьм первого =  "))
    t1 = float(input("Температура первого  "))
    v2 = float(input("Объёьм второго  "))
    t2 = float(input("Температура второго  "))
    # Формула объёма 2 добавленных жидкостей
    v = v1 + v2
    # Формула температуры образовавшейся смеси
    t = ((t1 * v1) + (t2 * v2)) / v
    # Конечный ответ
    print("v =  {:.4f}".format(v))
    print("t = {:.4f}".format(t))
# task5()
def task6():
    print("Задание №6")
    #Функция для вычисления расстояния между двумя точками
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    #Координаты вершин треугольника
    # x1, y1 = 1, 1
    x1, y1 = int(input("х1 = ")),int(input("y1 = "))
    x2, y2 = int(input("х2 = ")),int(input("y2 = "))
    x3, y3 = int(input("х3 = ")),int(input("y3 = "))
    #Вычисление длин сторон треугольника
    a = distance(x2, y2, x3, y3)
    b = distance(x1, y1, x3, y3)
    c = distance(x1, y1, x2, y2)
    # Вычисление полупериметра
    p = (a + b + c) / 2
    # Вычисление радиуса окружности вписанной в треугольник
    radius = ((p - a) * (p - b) * (p - c) / p) ** 0.5
    # Конечный ответ
    print("Радиус окружности = ","{:.4f}".format(radius))
#task6()
def task7():
  00  print("Задание №7")
    # Заданные коэффициенты:
    A1 = float(input("введи А1: "))
    B1 = float(input("введи В1: "))
    C1 = float(input("введи С1: "))
    A2 = float(input("введи А2: "))
    B2 = float(input("введи В2: "))
    C2 = float(input("введи С2: "))
    # Формула и решение
    D = A1 * B2 - A2 * B1
    x = (C1 * B2 - C2 * B1) / D
    y = (A1 * C2 - A2 * C1) / D
    # Конечный ответ
    print("Вычисляем x =","{:.4f}".format(x), "Вычисляем y =", "{:.4f}".format(y))
#task7()
def task8():
    print("Задание №8")
    # Значение данных
    V1 = float(input("Введите скорость 1-го авто(в км/ч): "))
    V2 = float(input("Введите скорость 2-го авто(в км/ч): "))
    S1 = float(input("Введите расстояние между авто(в км): "))
    T1 = float(input("Введите время(в часах): "))
    # if V1,V2,S1,T1  >= 1 and <= 100 :
    if 1 <= V1 <= 100 and 1 <= V2 <= 100 and 1 <= S1 <= 100 and 1 <= T1 <= 100:
        # Формула и вычисления S = S1+S2
        S2 = S1 + (T1 * (V1 + V2))
        a = "{:.4f}".format(S2)
        S11 = S2 + S1 #формула из условии
        b = "{:.4f}".format(S11)
        #Конечный ответ
        print("Общая дистанция = ", a, "км")
        print("Расстояние между машинами", b, "км")
    else:
        print("Введите число только : 1 ≤ V1, V2 , S, T ≤ 100")
# task8()
def task9():
    print("Задание №9")
    # Значение данных
    part_first = float(input("Вклад 1: "))
    part_second = float(input("Вклад 2: "))
    profit = float(input("Прибыль : "))
    koeficient = profit /(part_first+part_second)
    profit_first = part_first * koeficient
    profit_second = part_second * koeficient
    # Конечный ответ
    print("Вычисляем 1 ", profit_first)
    print("Вычисляем 2 ", profit_second)
#task9()

