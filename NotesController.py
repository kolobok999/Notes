import datetime


def input_note() -> list[str]:
    notes = list()
    notes.append(input("Введите заголовок: "))
    notes.append(input("Введите заметку: "))
    date = datetime.date.today()
    notes.append(f'{date.day}.{date.month}.{date.year}')
    return notes


def get_action():
    return input('Выберите действие: ').upper()


class NotesController:
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def run_notes(self):
        self.view.print_start_message()

        while True:
            action = get_action()
            if action == 'Q':
                break
            elif action == 'A':
                self.model.notes = self.model.create(input_note())
                self.view.print_message(f'Добавили заметку '
                                        + f'{self.model.notes[len(self.model.notes) - 1][0]}')
            elif action == 'P':
                self.view.print_notes(self.model.notes)
            elif action == 'E':
                self.model.export_notes(input("Введите имя файла для экспорта: "))
            elif action == 'I':
                self.model.notes = self.model.import_notes(input("Введите имя файла для импорта: "))
            elif action == 'F':
                idx = self.model.find(input('Введите тему заметки: '))
                if idx is None:
                    self.view.print_message('Такой заметки нет.')
                else:
                    self.view.print_message(f'{self.model.notes[idx][0]} '
                                            + f'{self.model.notes[idx][1]} '
                                            + f'{self.model.notes[idx][2]}')
            elif action == 'D':
                print(f'Удаляем: {self.model.delete(input("Введите id или заголовок удаляемой заметки: "))}')
            elif action == 'U':
                self.model.update(input('Введите заголовок обновляемой заметки: '), input_note())
            else:
                self.view.print_message("Ни одна из команд не подходит. Давайте попробуем ещё раз.")
