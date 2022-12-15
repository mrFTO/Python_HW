# 3'. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Запрашиваем последовательность чисел и кладем ее переменную num в числовом формате используя для их разделения функцию split
num = list(map(int, input('Please enter a sequence of numbers separated by a space: ').split()))
# # Выводим результат в виде списка с сортировкой уникальных элементов при помощи функции set
# print(f'A list of non-repeating elements of the entered sequence: {list(set(num))}')
# Новое решение с использованием lambda
list_filter = list(filter(lambda i: not ((i in num[: num.index(i)]) or (i in num[num.index(i) + 1:])), num))
print(f'The given sequence {num} contains the following non-repeating numbers: {list_filter}.')
