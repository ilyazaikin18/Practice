#  **Пример 2:** *Записать в txt файл свои данные и сохранить его в отдельную папку в проекте.*

import os
folder_path = 'C:/Users/Илья/Desktop/New_folder'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_path = os.path.join(folder_path, 'Exercise_6_1.txt')

with open(file_path, 'w') as f:
    f.write('Мои данные находятся здесь')
print(f'Данные пересохранены в этот файл: {file_path}')