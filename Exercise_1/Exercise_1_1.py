# Строковые операторы (экранирование, конкатенация, повторение строки, обращение по индексу, извлечение среза, длина
# строки, `find`, `index`, `replace`, `split`, `isdigit`, `isalpha`, `isalnum`, `islower`, `isupper`, `isspace`,
# `istitle`, `upper`, `lower`, `join`, `count`, `expandtabs`, `strip(l and r)`, `title`, `format`)

# Метод find() находит первое вхождение указанного значения.
# Метод find() возвращает -1, если значение не найдено.
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# Метод index() возвращает позицию при первом появлении указанного значения.
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")

# Метод replace() заменяет указанную фразу другой указанной фразой.
# Примечание. Все вхождения указанной фразы будут заменены, если не указано иное.
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

# Метод split() разбивает строку на список.
# Вы можете указать разделитель, по умолчанию разделителем является любой пробел.
# Примечание. Если указано значение maxsplit, список будет содержать указанное количество элементов плюс один.
txt = "welcome to the jungle"
x = txt.split()
print(x)

# Метод isdigit() возвращает True, если все символы являются цифрами, иначе False.
# Показатель степени, например ², также считается цифрой.
txt = "50800"
x = txt.isdigit()
print(x)

# Метод isalpha() возвращает значение True, если все символы являются буквами алфавита (az).
# Пример символов, не являющихся буквами алфавита: (пробел)!#%&? и т. д.
txt = "CompanyX"
x = txt.isalpha()
print(x)

# Метод isalnum() возвращает значение True, если все символы являются буквенно-цифровыми, то есть буквами алфавита (az)
# и цифрами (0–9).
# Пример символов, которые не являются буквенно-цифровыми: (пробел)!#%&? и т. д.
txt = "Company12"
x = txt.isalnum()
print(x)

# Метод islower() возвращает True, если все символы в нижнем регистре, иначе False.
# Цифры, символы и пробелы не проверяются, только буквы алфавита.
txt = "hello world!"
x = txt.islower()
print(x)

# Метод isupper() возвращает True, если все символы в верхнем регистре, иначе False.
# Цифры, символы и пробелы не проверяются, только буквы алфавита.
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

# Метод isspace() возвращает True, если все символы в строке являются пробелами, в противном случае — False.
txt = "   "
x = txt.isspace()
print(x)

# Метод istitle() возвращает True, если все слова в тексте начинаются с прописной буквы, а остальная часть слова —
# строчными буквами, в противном случае — False.
# Символы и цифры игнорируются.
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

# Метод upper() возвращает строку, в которой все символы в верхнем регистре.
#  Символы и цифры игнорируются.
txt = "Hello my friends"
x = txt.upper()
print(x)

# Метод lower() возвращает строку, в которой все символы в нижнем регистре.
#  Символы и цифры игнорируются.
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

# Метод join() берет все элементы в итерируемом объекте и объединяет их в одну строку.
# В качестве разделителя должна быть указана строка.
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

# Метод count() возвращает количество элементов с указанным значением.
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")

# Метод expandtabs() устанавливает размер табуляции на указанное количество пробелов.
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

# Метод lstrip() удаляет все начальные символы (пробел является начальным символом по умолчанию для удаления)
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

# Метод rstrip() удаляет все конечные символы (символы в конце строки), пробел — это удаляемый завершающий символ по
# умолчанию.
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

# Метод title() возвращает строку, в которой первый символ в каждом слове является прописным. Как заголовок или
# название.
# Если слово содержит число или символ, первая буква после этого будет преобразована в верхний регистр.
txt = "Welcome to my world"
x = txt.title()
print(x)

# Метод format() форматирует указанные значения и вставляет их в заполнитель строки.
# Заполнитель определяется с помощью фигурных скобок: {}. Подробнее о заполнителях читайте в разделе «Заполнители» ниже.
# Метод format()возвращает отформатированную строку.
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))