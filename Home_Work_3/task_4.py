# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# Создаем переменную num в которой будет введенное пользователем число в числовом формате
num = int(input('Please enter a decimal number: '))
x = '' # создаем пустую переменную x в которой будет результат преобразования в двоичное число
while num != 0: # используем цикл while для преобразования введенного пользователем числа в двоичное
    x = str(num % 2) + x
    num //= 2
# Отображаем результат преобразования
print(f'Received binary number: {x}')
