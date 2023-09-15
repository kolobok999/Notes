from os.path import join, abspath, dirname

MAIN_DIR = abspath(dirname(__file__))


class NotesModel:

    def __init__(self):
        self.notes: dict = {0: ["Title1", "note1", "15.09.2023"],
                            1: ["Title2", "note2", "15.09.2023"]}

    def create(self, note_list: list) -> dict:
        note_list = note_list
        size = len(self.notes)
        self.notes[size] = note_list
        return self.notes

    def export_notes(self, file_name: str):
        full_name = join(MAIN_DIR, "data", file_name + '.csv')

        with open(full_name, mode="w", encoding="UTF-8") as file:
            for idx, value in self.notes.items():
                file.write(f'{idx};{value[0]};{value[1]};{value[2]}\n')

    def import_notes(self, file_name: str) -> dict:
        full_name = join(MAIN_DIR, "data", file_name + '.csv')
        with open(full_name, mode='r', encoding='UTF-8') as file:
            for line in file:
                note_list = line.strip().split(';')
                self.notes.update(self.create(note_list[1:]))
        return self.notes

    def find(self, search: str):
        for idx, note_list in self.notes.items():
            title = note_list[0]
            if title.upper().startswith(search.upper()):
                return idx

    def update(self, upd: str, note_list):
        idx = self.find(upd)
        self.notes[idx] = note_list

    def delete(self, deleting: str):
        if deleting.isdigit():
            deleting = int(deleting)
        if isinstance(deleting, int):
            note_list = self.notes.pop(deleting, 'Такого id нет')
            self.update_idx()
            return note_list
        if isinstance(deleting, str):
            note_list = self.notes.pop(
                self.find(deleting), 'Такого заголовка нет')
            self.update_idx()
            return note_list

    def update_idx(self):
        idx = 0
        notations = self.notes.copy()
        self.notes.clear()
        for value in notations.values():
            self.notes[idx] = value
            idx += 1
