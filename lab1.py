
import math

def task1():
    # Задание 1
    #Значение х у z
    x = 1
    y = 9
    z = 3

    #Вычисление а
    #Числительные дроби
    a_up = (x**0.5)-(abs(y**0.25))

    #Знаменатели дроби
    a_down = x - math.log2(y)

    #Дробь
    a = a_up / a_down

    #Вычисление b
    b_1 = math.tan((x-1)**0.5)
    b_2 = abs(z)**1/3
    b_3 = (y**1/6) + x

    b = b_1 - b_2 - b_3
    print("Задание №1")
    print("Вычисляем a =", a )
    print("Вычисляем b =", b)

task1()

def task2():
    #Значение f(x)
    a = 5
    b = 2
    c = -5

    #Числительные дроби
    a_11 = (c*x)**0.5

    #Знаменатели дроби
    a_12 = b*x+a

    a_1 = a_11 / a_12
    a_2 = x**b

    #Дробь
    a = a_2 + a_1

    f = a
    print("Задание №2")
    print("Вычисляем f(x) =", a)
    print(a)

task2()

#3
# Значение f(x)

ab_1 = (math.cos**2 * (math.sin(1/(x**2))))



print("Вычисляем f(x) =",ab_1)
print(ab_1)



def task4():

    k = 2
    alfha = 60
    beta = 30
    gamma = 180 - (alfha+beta)

    S1 = 1/2*k**2
    S2 = math.sin(alfha)*math.sin(beta)/math.sin(gamma)
    S = S1 * S2
    print(S)
task4()

def task5():

    v1 = 5
    t1 = 100
    v2 = 5
    t2 = 10
    # Формула объёма
    v = v1 + v2
    # Формула температуры образовавшейся смеси
    t = ((t1*v1)+(t2*v2))/v
    print("Вычесляем объём:",v)
    print("Вычесляем температуру:",t)
task5()

def task6():

    # Функция для вычисления расстояния между двумя точками
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5

    # Координаты вершин треугольника
    x1, y1 = 1, 1
    x2, y2 = 2, 2
    x3, y3 = 4, 4

    # Вычисление длин сторон треугольника
    a = distance(x2, y2, x3, y3)
    b = distance(x1, y1, x3, y3)
    c = distance(x1, y1, x2, y2)

    # Вычисление полупериметра
    p = (a + b + c) / 2

    # Вычисление радиуса окружности вписанной в треугольник
    radius = ((p - a) * (p - b) * (p - c) / p)**0.5

    print("Радиус окружности вписанной в треугольник:", radius)
task6()


def task7():

    # Заданные коэффициенты:

    A1 = - 5
    B1 = 2
    C1 = 3

    A2 = 4
    B2 = 5
    C2 = 6

    #Формула и решение
    D = A1*B2-A2*B1
    x = (C1*B2-C2*B1)/D
    y = (A1*C2-A2*C1)/D
    print("Вычисляем x =", x)
    print("Вычисляем y =", y)

task7()





