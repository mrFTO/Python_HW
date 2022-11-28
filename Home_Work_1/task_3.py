# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#     Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# Создаем переменные x и y, в которые кладем запрошенные у пользователя числовые значения.
x = int(input('Please enter point X coordinates: '))
y = int(input('Please enter point Y coordinates: '))
# Если x и y равны нулю, то сообщаем что местонахождение точки найти не удалось.
if x == 0 and y == 0:
    print(
        f'X = {x}, Y = {y}. Error, the location of the point could not be determined.')
# Иначе, если x больше нуля и y больше нуля, то сообщаем, что точка находится в первой четверти.
elif x > 0 and y > 0:
    print(f'X = {x}, Y = {y}. The point is in the first quarter.')
# Иначе, если x меньше нуля и y больше нуля, то сообщаем, что точка находится во второй четверти.
elif x < 0 and y > 0:
    print(f'X = {x}, Y = {y}. The point is in the second quarter.')
# Иначе, если x меньше нуля и y меньше нуля, то сообщаем, что точка находится в третьей четверти.
elif x < 0 and y < 0:
    print(f'X = {x}, Y = {y}. The point is in the third quarter.')
# Иначе, если x больше нуля и y меньше нуля, то сообщаем, что точка находится в четвертой четверти.
elif x > 0 and y < 0:
    print(f'X = {x}, Y = {y}. The point is in the fourth quarter.')
# Иначе, если x равен нулю, то сообщаем, что точка находится на оси y.
elif x == 0:
    print(f'X = {x}, Y = {y}. The point is on the y-axis.')
# Иначе, если y равен нулю, то сообщаем, что точка находится на оси x.
elif y == 0:
    print(f'X = {x}, Y = {y}. The point is on the x-axis.')
