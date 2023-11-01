while True:
    # ваш код, который нужно повторять
    password = input("Your password please")
    if password == "112233":
        print("Welcome")
    else:
        print("Wrong !")
    # проверяем условие для выхода из бесконечного цикла (например, при вводе "q")
    if input("Хотите выйти? (y/n): ") == "y":
        break  # выходим из цикла
    
