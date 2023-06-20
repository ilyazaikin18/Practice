# **Пример 1:** *Прочитать txt файл и вывести его на экран.*

f = open('C:/Users/Илья/Desktop/Exercise_6.txt', 'r')
read = f.readline()
print(read, end='')
f.close()