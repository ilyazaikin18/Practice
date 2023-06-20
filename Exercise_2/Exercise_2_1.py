# **Пример 2**: *Проверка на число больше, меньше или равно нулю*
number = int(input('Введите число: '))
if number == 0:
    print(number, 'Это число равно нулю')
elif number > 0:
    print(number, 'Это число больше 0')
else:
    print(number, 'Это число меньше 0')