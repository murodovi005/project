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





import random


def get_user_choice():
    user_choice = input("Выберите: камень (r), ножницы (s), бумага (p): ")
    if user_choice in ['r', 's', 'p']:
        return user_choice
    else:
        print("Неверный выбор. Попробуйте снова.")
        return get_user_choice()


def get_computer_choice():
    choices = ['r', 's', 'p']
    computer_choice = random.choice(choices)
    return computer_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (
            (user_choice == 'r' and computer_choice == 's') or
            (user_choice == 's' and computer_choice == 'p') or
            (user_choice == 'p' and computer_choice == 'r')
    ):
        return "Вы победили!"
    else:
        return "Компьютер победил!"


def main():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Ваш выбор: {user_choice}")
        print(f"Выбор компьютера: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Хотите сыграть еще раз? (y/n): ")
        if play_again.lower() != 'y':
            break

    print("Спасибо за игру!")


if __name__ == "__main":
    main()
import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
window_width = 800
window_height = 600
cell_size = 20

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Змейка")

# Инициализация змейки
snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = (cell_size, 0)

# Инициализация еды
food = (random.randrange(1, (window_width // cell_size)) * cell_size,
        random.randrange(1, (window_height // cell_size)) * cell_size)

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, cell_size):
                snake_direction = (0, -cell_size)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -cell_size):
                snake_direction = (0, cell_size)
            elif event.key == pygame.K_LEFT and snake_direction != (cell_size, 0):
                snake_direction = (-cell_size, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-cell_size, 0):
                snake_direction = (cell_size, 0)

    # Движение змейки
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    # Проверка столкновения с едой
    if snake[0] == food:
        food = (random.randrange(1, (window_width // cell_size)) * cell_size,
                random.randrange(1, (window_height // cell_size)) * cell_size)
    else:
        snake.pop()

    # Проверка столкновения с границами
    if (snake[0][0] < 0 or snake[0][0] >= window_width or
            snake[0][1] < 0 or snake[0][1] >= window_height):
        running = False

    # Проверка столкновения с самой собой
    if snake[0] in snake[1:]:
        running = False

    # Очистка экрана
    screen.fill(black)

    # Отрисовка змейки
    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], cell_size, cell_size))

    # Отрисовка еды
    pygame.draw.rect(screen, red, (food[0], food[1], cell_size, cell_size))

    pygame.display.update()

    # Ограничение частоты обновления экрана
    pygame.time.Clock().tick(10)

# Завершение игры
pygame.quit()


import pygame

# Инициализация Pygame
pygame.init()

# Параметры окна
window_width = 800
window_height = 600

# Цвета
white = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Игра Марио")

# Инициализация персонажа Марио
mario_x = 100
mario_y = 400
mario_speed = 5
jump = False
jump_height = 10

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление Марио
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario_x -= mario_speed
    if keys[pygame.K_RIGHT]:
        mario_x += mario_speed
    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jump_height >= -10:
            neg = 1
            if jump_height < 0:
                neg = -1
            mario_y -= (jump_height ** 2) * 0.5 * neg
            jump_height -= 1
        else:
            jump = False
            jump_height = 10

    # Очистка экрана
    screen.fill(white)

    # Отрисовка Марио
    pygame.draw.rect(screen, (255, 0, 0), (mario_x, mario_y, 50, 50))

    pygame.display.update()

# Завершение игры
pygame.quit()


import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
window_width = 800
window_height = 600

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Поймай мячи")

# Инициализация игрока
player_width = 50
player_height = 50
player_x = (window_width - player_width) // 2
player_y = window_height - player_height

# Инициализация мячей
ball_width = 50
ball_height = 50
ball_x = random.randint(0, window_width - ball_width)
ball_y = 0
ball_speed = 5

# Основной цикл игры
running = True
score = 0
font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

    # Движение мячей
    ball_y += ball_speed

    # Обработка столкновения с игроком
    if player_x < ball_x + ball_width and player_x + player_width > ball_x:
        if player_y < ball_y + ball_height and player_y + player_height > ball_y:
            ball_x = random.randint(0, window_width - ball_width)
            ball_y = 0
            score += 1

    # Если мяч упал за нижний край экрана
    if ball_y > window_height:
        ball_x = random.randint(0, window_width - ball_width)
        ball_y = 0

    # Очистка экрана
    screen.fill(white)

    # Отрисовка игрока
    pygame.draw.rect(screen, red, (player_x, player_y, player_width, player_height))

    # Отрисовка мячей
    pygame.draw.rect(screen, red, (ball_x, ball_y, ball_width, ball_height))

    # Отображение счета
    text = font.render("Счет: " + str(score), True, red)
    screen.blit(text, (10, 10))

    pygame.display.update()

# Завершение игры
pygame.quit()

import random

# Список вопросов и ответов
вопросы = [
    {
        "вопрос": "Какая планета является ближайшей к Солнцу?",
        "ответ": "Меркурий"
    },
    {
        "вопрос": "Какой город является столицей Франции?",
        "ответ": "Париж"
    },
    {
        "вопрос": "Сколько месяцев в году имеют 28 дней?",
        "ответ": "12"
    },
    {
        "вопрос": "Какой химический элемент обозначается как 'O'?",
        "ответ": "Кислород"
    }
]

def run_quiz():
    random.shuffle(вопросы)
    score = 0

    for вопрос_и_ответ in вопросы:
        вопрос = вопрос_и_ответ["вопрос"]
        правильный_ответ = вопрос_и_ответ["ответ"]

        print(вопрос)
        ответ_пользователя = input("Ваш ответ: ")

        if ответ_пользователя.lower() == правильный_ответ.lower():
            print("Правильно!")
            score += 1
        else:
            print("Неправильно. Правильный ответ:", правильный_ответ)

        print()

    print("Игра завершена. Вы набрали", score, "из", len(вопросы), "баллов.")

if __name__ == "__main__":
    print("Добро пожаловать в викторину!")
    run_quiz()







def task2():
    print('Задание 2')
    a = 5
    b = 2
    c = -5
    x = float(input("введи x: "))

    # Числительные дроби
    up = (c * x) ** 0.5
    down = (b * x) + a
    # Дробь
    f_1 = up / down
    f_2 = x ** b

    f = f_2 + f_1
    print("{:.4f}".format(f))

