# 1. Создайте программу для игры с конфетами человек против человека.
# ' Условие задачи: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

# Импортируем функции random и randint
from random import randint

# Создаем функцию, которая будет определять сколько конфет берет игрок и возвращает полученное значение в переменной x
def move_counter(name):
    x = int(
        input(f'{name}, please choose and take from 1 to 28 candies on the table: '))
    while x < 1 or x > 28:
        x = int(
            input(f'{name}, you are taking the wrong amount of candies. Please choose and take from 1 to 28 candies: '))
    return x

# Создаем функцию, которая будет выводить результаты хода игрока
def status(name, k, counter, candies):
    print(f'Player {name} made a move, he took {k} candies, now he has {counter} candies. There are {candies} candies left on the table.')


# Запрашиваем у пользователя имена для 1 и 2 игроков
player1 = input("Please enter the name for the first player: ")
player2 = input("Please enter the name for the second player: ")

# количество конфет в игре.
candies = 117
# candies = int(input("Please enter the amount of candies on the game table: ")) # можно также запросить у пользователя количество конфет для повышения вариативности.))

# Используем функцию randint для определения очередности хода
turn_order = randint(0, 2)
if turn_order:
    print(f"{player1} makes the first move")
else:
    print(f"{player2} makes the first move")

# создаем переменные для хранения количества конфет у игроков в процессе игры
counter1 = 0
counter2 = 0

# создаем алгоритм расчета конфет в игре для игроков, с использованием цикла while и условных операторов if-else
while candies > 28:
    if turn_order:
        k = move_counter(player1)
        counter1 += k
        candies -= k
        turn_order = False
        status(player1, k, counter1, candies)
    else:
        k = move_counter(player2)
        counter2 += k
        candies -= k
        turn_order = True
        status(player2, k, counter2, candies)

# Выводим сообщение, кто победил в игре.
if turn_order:
    print(f'{player1} won!!!')
else:
    print(f'{player2} won!!!')
