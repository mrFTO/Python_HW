# # 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Создаем переменную my_list, в которой будет список из примера для расчета
my_list = [2, 3, 5, 9, 3]
# Создадим функцию, которая будет искать нечетные элементы в заданном списке, складывать их и показывать результат
def count_list(list):
    x = 0 # переменная в которой будет храниться результаты расчета
    for i in range(len(list)):  # для i в диапазоне длинны листа
        if i %  2 != 0: # если остаток от деления i на 2 не равен нулю 
            x = x + list[i] # то складываем значение переменной x со значением списка под индексом i
    print(f'The sum of the list elements in an odd position is {x}.') # отображаем полученную сумму нечетных элементов заданного списка

count_list(my_list) # Запускаем функцию для нашего списка


