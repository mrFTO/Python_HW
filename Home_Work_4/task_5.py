# 5'. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9 

from random import Random, randint # импортируем функции

list = [] # Создаем пустой лист
 # Открываем файлы с атрибутом запись
f1 = open('polynomial_1.txt', 'w') # первый многочлен
f2 = open('polynomial_2.txt', 'w') # второй многочлен
f3 = open('sum_polynomial.txt', 'w') # сумма многочленов

for i in range(8):
    num = randint(0, 100)
    list.append(num)
# создание первого многочлена
polynomial1 = f'{list[0]}*x^{list[1]} + {list[2]}*x^{list[3]}'
f1.write(str(polynomial1))
f1.close()
# создание второго многочлена
polynomial2 = f'{list[4]}*x^{list[5]} + {list[6]}*x^{list[7]}'
f2.write(str(polynomial2))
f2.close()

file1 = 'polynomial_1.txt'
file2 = 'polynomial_2.txt'
fil1 = open(file1, 'r')
fil2 = open(file2, 'r')

for line1 in fil1:
    line1
for line2 in fil2:
    line2
# запись суммы многочленов
sum_polynomial = f'({line1}) + ({line2})'
f3.write(str(sum_polynomial))
# Вывод получившегося выражения
print(f'({line1}) + ({line2})')
fil1.close()
fil2.close()
f3.close()
