def task1():
    a = float(input("введи a: "))
    if a % 2 == 0:
        print('Четное число')
    else:
        print('Нечентное число')

# task1()


def task1():
    def numb(b):
        '''1.Определение чётности чисел'''

        if b % 2 == 0:
            return True
        else:
            return False

    # 2.Определени палиндром
    def palindrom(a):
        a3 = a % 10
        a2_1 = (a - a3)
        a2 = (a2_1 / 10) % 10
        a1 = (a2_1 / 10 - a2) / 10
        print(a1, a2, a3)
        if a1 == a3:
            return True
        else:
            return False

    x = input()
    palindrom(x)
    numb(x)
    if palindrom(x) == True:
        print("Палиндром")
    else:
        print("не Палиндром")

    if numb(x) == True:
        print("Чётное число ")
    else:
        print("Не чётное число ")


task1()

