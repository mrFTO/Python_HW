# 1'. Вычислить число Пи c заданной точностью d
# Пример: 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

from math import pi # импортируем значение числа Пи из библиотеки math.

# Просим пользователя задать точность для числа Пи в указанном формате.
d = input("Please enter a number to determine the precision of π:\n*in the format 0.1 or 0.01 or 0.001 etc.\n**Using letters or a comma instead of a dot will cause an error in this program! (ﾉ>ω<)ﾉ :｡･:*:･ﾟ’★,｡･:*:･ﾟ’☆\n--> ")
# Если пользователь ввел не корректное значение параметра - выводим сообщение о неверном запросе и просим повторить ввод.
if float(d) >= 0.2:
    print('Invalid request.\nPlease enter a number to determine the precision of π (for example 0.1 or 0.01 or 0.001 etc).\nPlease, try again. (´• ω •`)ﾉ')
else: # Иначе сообщаем пользователю значение числа Пи с заданной точностью.
    print(f'The value of π with a given accuracy {d} will be equal to {round(pi, len(d) - 2)}') 
