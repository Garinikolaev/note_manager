username = input('Имя пользователя: ')
title1 = input('Заголовок заметки 1: ')
title2 = input('Заголовок заметки 2: ')
title3 = input('Заголовок заметки 3: ')
title = [title1, title2, title3]
content = input('Описание заметки: ')
status = input('Статус заметки: ')
created_date = input('Дата создания заметки в формате "день-месяц-год": ')
issue_date = input('Дата истечения заметки (дедлайн) в формате "день-месяц-год": ')
print('Имя пользователя: ', username)
print('Заголовок заметки: ', title)
print('Описание заметки: ', content)
print('Статус заметки:', status)
print('Дата создания заметки: ', created_date)
print('Дата истечения заметки: ', issue_date)