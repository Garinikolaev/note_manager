username = input('Введите имя пользователя: ')
title1 = input('Заголовок заметки 1: ')
title2 = input('Заголовок заметки 2: ')
title = [title1, title2]
content = input('Напишите описание заметки: ')
status = input('Проставьте статус заметки: ')
created_date = input('Дата создания заметки: ')
issue_date = input('Дата изменения заметки: ')
note = [username, title, content, status, created_date, issue_date]
print(note)