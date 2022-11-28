# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#     Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# Создаем переменные для координат двух точек по осям x и y и вносим в них числовые значения, введенные пользователем.
a_x = int(input('Please enter the coordinate of the point A along the x-axis: '))
a_y = int(input('Please enter the coordinate of the point A along the y-axis: '))
b_x = int(input('Please enter the coordinate of the point B along the x-axis: '))
b_y = int(input('Please enter the coordinate of the point B along the y-axis: '))
# Создаем переменную d, которой присваиваем результат расчета расстояния между заданными координатами точек A и B в 2D пространстве, округленный до двух знаков после запятой.
d = round(((b_x - a_x)**2 + (b_y - a_y)**2)**0.5, 2)
# Выводим указанные координаты точек и полученное расстояние.
print(f'The distance between point A with coordinates ({a_x}, {a_y}) and point B with coordinates ({b_x}, {b_y}) is {d}.')
