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

def task2():
    









a = input("Введи число:")
n = int(input("Выбери систему:"))

s = '' # Str
m = 'ABCDEF' # Massive

while a > 0:
    с1 = a % n
    if с1 > 9:
        s = hex(a)
    else:
        s = str(a % n) + s
        a //= n
print(s)





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


# task1()



#3

a = int(input("Введи число:"))
n = int(input("Выбери систему:"))

s = '' # Str

while a > 0:
    с = (a % n)
    if c < 10:
        s = str(a % n) + s
        a //= n
    else:
        s = hex(a)
print(s)





#6
def months_to_buy(cost,salary):
    month = input()
    if month > 1:

        salary = 50000
        cost = 200000
        growing_salary = 5 % salary

    month_price = salary + growing_salary
    final_cost = cost + (3.15 % salary)
    print(final_cost)

#bin двоичная
#oct восьмеричная
#hex шестнадцатеричная
def decimnal_in_new_numeral_system(number, base):
    if number < 0 or base < 2 or base > 36:
        return "Неверные входные данные"
    result = ""
    while number > 0:
        s = number % base
        if s < 10:
            result = str(s) + result
        else:
            result = chr(ord('A') + s - 10) + result
        number //= base
    return result if result else "0"
number = int(input("Введи число в десятичной системе : "))
users = int(input("Введи основание новой системы счисления (от 2 до 36): "))
result = decimnal_in_new_numeral_system(number, users)
print(f"Результат перевода: {result}")






def decimal_to_base(num, base):
    if num == 0:
        return '0'
    res = ''
    while num > 0:
        remainder = num % base
    if remainder < 10:
        res = str(remainder) + res
    else:
        res = chr(remainder + 55) + res
        num = num // base
    return res

def fraction_to_base(num, base, precision):
    res = ''
    for _ in range(precision):
        num *= base
        integer_part = int(num)
    if integer_part < 10:
        res += str(integer_part)
    else:
        res += chr(integer_part + 55)
        num -= integer_part
    return res

decimal_number = float(input("Введите десятичную дробь: "))
base = int(input("Введите основание системы счисления: "))
precision = int(input("Введите точность округления: "))

integer_part = int(decimal_number)
fractional_part = decimal_number - integer_part

integer_in_base = decimal_to_base(integer_part, base)
fraction_in_base = fraction_to_base(fractional_part, base, precision)

print(f"Десятичная дробь {decimal_number} в системе счисления с основанием {base}: {integer_in_base}.{fraction_in_base}")


def decimal_to_base(numer, denom, base):
    # Перевод числителя в заданную систему счисления
    integer_part = ""
    while numer > 0:
        remainder = numer % base
        integer_part = str(remainder) + integer_part
        numer //= base

    # Если знаменатель не равен 1, переводим дробную часть
    if denom != 1:
        fractional_part = "."
        fractional_remainders = set()
        while numer != 0:
            numer *= base
            quotient = numer // denom
            remainder = numer % denom
            fractional_part += str(quotient)
            if remainder in fractional_remainders:
                break
            fractional_remainders.add(remainder)
            numer = remainder
        return integer_part + fractional_part
    else:
        return integer_part
numer = int(input("Введите числитель дроби: "))
denom = int(input("Введите знаменатель дроби: "))
base = int(input("Введите систему счисления (2-16): "))
result = decimal_to_base(numer, denom, base)
print(f"Результат перевода: {result}")




#Правильный вариант
def decimal_in_new_numeral_system(num, base):
    if num == 0:
        return '0'
    res = ''
    while num > 0:
        remainder = num % base
    if remainder < 10:
        res = str(remainder) + res
    else:
        res = chr(remainder + 55) + res
        num = num // base
    return res
def fraction_to(num, base,):
    res = ''
    integer_part = int(num)
    if integer_part < 10:
        res += str(integer_part)
    else:
        res += chr(integer_part + 55)
        num -= integer_part
    return res
decimal_number = float(input("Введите десятичную дробь: "))
base = int(input("Введите основание системы счисления: "))
integer_part = int(decimal_number)
fractional_part = decimal_number - integer_part
integer_in_base = decimal_to_base(integer_part, base)
fraction_in_base = fraction_to_base(fractional_part, base, precision)
print(f"Десятичная дробь {decimal_number} в системе счисления с основанием {base}: {integer_in_base}.{fraction_in_base}")



