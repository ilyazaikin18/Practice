# **Пример 1**: *Проверка числа на четность*.
number = int(input('Введите любое число: '))
if number % 2 == 0:
    print(number, 'Это число четное')
else:
    print(number, 'Это число нечетное')