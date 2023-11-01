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


#2
import time

while True:
    # Ваш код здесь
    print("Привет, мир!")

    # Создайте задержку в 1 секунду перед следующей итерацией
    time.sleep(5)
