notes = [
    {
        'name': 'Алексей',
        'title': 'Список покупок',
        'description': 'Купить продукты на неделю'
    },
    {
        'name': 'Мария',
        'title': 'Учеба',
        'description': 'Подготовиться к экзамену'
    }
]

def display_notes():
    # Отображает все текущие заметки
    if not notes:
        print("Нет заметок.")
        return

    print("\nТекущие заметки:")
    for i, note in enumerate(notes):
        print(f"{i + 1}.")
        print(f"\tИмя: {note['name']}")
        print(f"\tЗаголовок: {note['title']}")
        print(f"\tОписание: {note['description']}\n")


def delete_note(criterion):
    # Удаляет заметку по заданному критерию (имя или заголовок)
    found = False
    for i, note in enumerate(notes):
        if criterion in (note['name'], note['title']):
            del notes[i]
            found = True
            break

    if found:
        print("\nУспешно удалено. Остались следующие заметки:\n")
        display_notes()
    else:
        print("\nЗаметок с таким именем пользователя или заголовком не найдено.\n")


if __name__ == "__main__":
    # Отображение текущих заметок
    display_notes()

    # Запрашиваем у пользователя критерий для удаления
    while True:
        criterion = input("Введите имя пользователя или заголовок для удаления заметки: ")

        # Удаляем заметку
        delete_note(criterion)