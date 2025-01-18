from datetime import datetime
current_date = "27-11-2024"
print("Текущая дата: ", current_date)
current_date = datetime.strptime(current_date, "%d-%m-%Y") # Преобразуем строку в объект даты
issue_date = input("Введите дату дедлайна (в формате день-месяц-год): ") # Запрашиваем у пользователя дату дедлайна
issue_date = datetime.strptime(issue_date, "%d-%m-%Y") # Преобразуем строку в объект даты
try:
    delta_days = (issue_date - current_date).days # Вычисляем разницу между текущей датой и дедлайном
    if delta_days > 0:
        print("До дедлайна осталось", delta_days, "дней.")
    elif delta_days == 0:
        print("Сегодня последний день для выполнения задания!")
    else:
        print("Внимание! Дедлайн истёк", delta_days, "дней назад.")
except ValueError:
    print("Неверный формат даты. Пожалуйста, введите дату в правильном формате.")