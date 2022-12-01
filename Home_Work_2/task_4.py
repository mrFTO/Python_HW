# 4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2
#  Создадим переменную n, в которую положим полученное от пользователя значение в числовом формате.
n = int(input('Please enter a value for the number N: '))
# Создадим пустой список.
list = []
# Запустим цикл, который наполнит список числами из промежутка [-N, N].
for i in range(-n, n+1):
    list.append(i)
# Выведем полученный список.
print(f'Created a list from -{n} to {n} is {list}.')
# Запросим ввод позиций через запятую для дальнейшего расчета произведения элементов.
listElement = input('Please enter the positions of the elements of the list separated by commas to calculate the product of the elements: ')
splitList = listElement.split(",")
positionElement = []
for i in splitList:
    positionElement.append(int(i))
# Зададим переменные x и y, в которых будут храниться выбранные позиции(y) и результат их умножения(x).
x = 1
y = 0
# Для наглядности, выведем значения выбранных позиций.
print('Positions selected for calculation: ')
# Запустим цикл, который найдет произведение элементов на указанных позициях.
for i, i in enumerate(positionElement):
    y = list[i]
    x *= y
    print(y)
# Выведем результат произведения.
print(f'The product of the elements at the selected positions is: {x}')
