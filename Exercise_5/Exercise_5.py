# **Пример 1:** *Создать класс "Животное" с полями "Имя", "Возраст". Сделать функции через которые можно изменять имя
# и возраст животного. Создать экземпляр класса cat, дать имя и возраст животному. Вывести в консоль результат, ниже
# изменить возраст животного. Сделать проверку на то что бы у животного не было отрицательного возраста*

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    def check_age(self, check):
        if check >= 0:
            return True
        else:
            return False

Cat = Animal('Боря', 10)

Cat.set_name('Вася')
Cat.set_age(5)

print(f"Имя: {Cat.name}, Возраст: {Cat.age}")