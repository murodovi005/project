
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

ab_1 = (math.cos**2 * (math.sin(1/(x**2))



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







