username = input('Введите имя пользователя: ')
title1 = input('Заголовок заметки 1: ')
title2 = input('Заголовок заметки 2: ')
titles = [title1, title2]
content = input('Напишите описание заметки: ')
status = input('Проставьте статус заметки: ')
created_date = input('Введите дату создания заметки: ')
issue_date = input('Введите дату изменения заметки: ')
note = [username,
        [title1,
        title2],
        content,
        status,
        created_date,
        issue_date]
print('Имя пользователя: ', username)
print('Заголовок заметки 1: ', title1)
print('Заголовок заметки 2: ', title2)
print('Описание заметки: ', content)
print('Статус заметки:', status)
print('Дата создания заметки: ', created_date)
print('Дата истечения заметки: ', issue_date)