def project1():
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
project1()


def project2():
    import tkinter as tk
    from PIL import Image, ImageTk

    # Создание главного окна
    window = tk.Tk()

    # Загрузка изображения
    image = Image.open("example.jpg")
    image = image.resize((400, 300))  # Изменение размера изображения

    # Конвертация изображения для использования в Tkinter
    tk_image = ImageTk.PhotoImage(image)

    # Создание виджета для отображения изображения
    image_label = tk.Label(window, image=tk_image)
    image_label.pack()

    # Запуск главного цикла окна
    window.mainloop()
project2()


def project3():
    import time

    while True:
        # Ваш код здесь
        print("Привет, мир!")

        # Создайте задержку в 1 секунду перед следующей итерацией
        time.sleep(5)
project3()





import math

def calculate_area(k, alpha, beta):
    # перевод градусов в радианы
    alpha = math.radians(alpha)
    beta = math.radians(beta)
    
    # вычисление высоты треугольника
    h = k * math.sin(beta)
    
    # вычисление площади треугольника
    area = (k * h) / 2
    
    return area

# пример использования функции
k = 5
alpha = 45
beta = 60
triangle_area = calculate_area(k, alpha, beta)
print("Площадь треугольника:", triangle_area)
