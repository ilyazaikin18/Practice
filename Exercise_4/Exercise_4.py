# **Пример 1: ** *Создать функцию которая вычисляет площадь поверхности шара, объем шара с применением  математической
# библиотеки. Сделать цикл который будет выполнять эту функцию от 1 до числа которое вы введете и будет вносить
# результат функции в список словарей: [[{"Площадь": Значение},{"Объем": Значение}],[{"Площадь": Значение},
# {"Объем": Значение}]]

from math import *
def ball(radius):
    S = 4 * pi * (radius ** 2)
    V = (4 / 3) * pi * (radius * 2)
    return [{'Площадь': S}], [{'Объём': V}]

number = int(input('Введите любое число: '))
res = []

for i in range(1, number + 1):
    res.append(ball(i))
print(res)