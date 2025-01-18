class Note:
    def __init__(self, user_name, title, description, status, creation_date, deadline):
        self.user_name = user_name
        self.title = title
        self.description = description
        self.status = status
        self.creation_date = creation_date
        self.deadline = deadline

    def display_note(self):
        print(f"""
Имя: {self.user_name}
Заголовок: {self.title}
Описание: {self.description}
Статус: {self.status}
Дата создания: {self.creation_date}
Дедлайн: {self.deadline}
""")


def add_new_note():
    user_name = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    creation_date = input("Введите дату создания (день-месяц-год): ")
    deadline = input("Введите дедлайн (день-месяц-год): ")

    return Note(user_name, title, description, status, creation_date, deadline)


def main():
    notes = []

    print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")

    while True:
        note = add_new_note()
        notes.append(note)

        choice = input("\nХотите добавить ещё одну заметку? (да/нет): ").lower().strip()
        if choice == 'нет':
            break

    print("\nСписок заметок:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}.")
        note.display_note()


if __name__ == "__main__":
    main()