# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Создаем переменную my_list, в которой будет список из примера для расчета 
my_list = [1.1, 1.2, 3.1, 5.1, 10.01]
# Создаем функцию для поиска разницы между максимальным и минимальным значением дробной части элементов
def difference(list):
    x =[]
    for i in range(len(list)):
        x.append(list[i]%1)
    return max(x) - min(x)
#  Отображаем наш список и полученное в результате выполнения функции для поиска разницы между максимальным и минимальным значением дробной части элементов
print(f'{my_list} -> {round(difference(my_list), 2)}')
