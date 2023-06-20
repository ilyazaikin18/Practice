# **Пример 3:** *Прочитать txt файл и заменить первое предложение в нем на свои значения.*
f = open('C:/Users/Илья/Desktop/Exercise_6.txt', 'r')
read = f.readline()
print(read, end='')

with open('C:/Users/Илья/Desktop/Exercise_6.txt', 'w') as f:
    f.write('Мои данные находятся здесь')
print(f"Данные пересохранены в этот файл: {'C:/Users/Илья/Desktop/Exercise_6.txt'}")
f.close()