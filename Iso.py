#1
import math
x = 1
y = 2
z = 3

a_11 = (abs(x**2-6))**0.5
a_12 = (abs(y**2-5))**0.5

a_up = a_11 - a_12

a_21 = 1+((x**2)/(y**3+1))
a_22 = (y**2)/(x**3+1)

a_down = a_21 + a_22

a = a_up / a_down

b_11 = x**3
b_12 = math.atan(z)**3 + math.exp(1)
b = b_11 * b_12
print("Вычисляем a =", a )
print("Вычисляем b =", b)












# #2
# import math
#
# a = 2
# b = -1
# c = 3
#
# a_1 = (x+a)**(1/3)
# a_2 = (c*x**2)/(b+x)
# a = a_1 + a_2
#
#
# def f{x}:
#     return a
# print(a)



















# #3
# import math
#
# x = 2
# x_1 = math.cos(math.sin(math.cos(1/(x**2))**2)**3)**2
# x_2 = abs((x**3)+3**x)
# x_11 = x_1 - x_2
#
#
#
#  print(x)