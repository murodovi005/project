def task7():
    import math
    x = float(input("x = "))
    eps = float(input("e = "))
    n = 1
    while  x > 0 and x < 0:
        degree_x = x +  x ** (2*n+1)/math.factorial(2*n+1)
    
        if x == 0:
            print("Ok")
            break
#task7
