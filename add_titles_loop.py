note = [] # Создали список
title = 0 # Создали переменную
while title != "": # Создали цикл
    title = input("Введите заголовок заметки или оставьте поле пустым (нажмите 'Enter'): ") # Запрашивает заголовок
    if title != "":
        note.append(title) # Добавляем заголовок в список
        continue
    else:
        print("Ввод заголовков завершён")
        break
print("Заголовки заметки:", *note, sep="\n - ") # Вывели список всех добавленных заголовков