# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#  6 -> [1,2,3]
#  144 -> [2,3]
# Создаем функцию которая будет возвращать список простых множителей числа N
def multi_list(n):
    my_list = []                # Создаем пустой список в котором будут находиться найденные множители
    for i in range(2, n):       # для диапазона от 2 до n
        while n % i == 0:       # пока остаток от деления будет равен нулю
            n /= i              # присваиваем n новое значение 
            my_list.append(i)   # положим в конец списка
    return my_list              # возвращаем получившийся список

n = int(input('Please enter a natural number for N: ')) # Запрашиваем у пользователя натуральное число и кладем в переменную n в числовом формате
# Выводим результат с учетом показа только уникальных делителей
print(f'The prime factors of the number {n} will be: {list(set(multi_list(n)))}')


