# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И".

# Создадим переменные x, y и z и запросим их значения у пользователя в числовом формате.

x = int(input('Please enter a value for variable X: '))
y = int(input('Please enter a value for variable Y: '))
z = int(input('Please enter a value for variable Z: '))

# Если не (x или y или z) равно (не x и не y и не z), то выводим сообщение, что утверждение истинно.
if not (x or y or z) == (not x and not y and not z):
    print(f'The statement ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is true.')

# Иначе, выводим сообщение, что утверждение ложно.
else:
    print(f'The statement ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is false.')
