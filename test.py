import turtle
import random

# Инициализация экрана
screen = turtle.Screen()
screen.title("Десять рыб")

# Загрузка изображения рыбы
screen.addshape("/Users/mvideomvideo/Desktop/fish.gif")

# Список для хранения рыб
fish_list = []

# Создание 10 рыб
for _ in range(11):
    fish = turtle.Turtle()
    fish.shape("/Users/mvideomvideo/Desktop/fish.gif")
    fish.color("blue")
    fish.penup()
    fish.speed(1)
    fish.setx(random.randint(-200, 200))
    fish.sety(random.randint(-200, 200))
    fish.shapesize(stretch_wid=0.025, stretch_len=0.025)  # Изменяем масштаб в 2 раза
    fish_list.append(fish)

# Функция для произвольного движения рыб
def move_randomly():
    for fish in fish_list:
        angle = random.randint(0, 360)
        distance = random.randint(1, 20)
        fish.setheading(angle)
        fish.forward(distance)

    # Вызываем функцию повторно через 100 миллисекунд
    screen.ontimer(move_randomly, 100)

# Запускаем функцию произвольного движения
move_randomly()

# Основной цикл программы
turtle.mainloop()



















