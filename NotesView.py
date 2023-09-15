class NotesView:
    def print_message(self, message: str) -> None:
        print(message)

    def print_start_message(self) -> None:
        print("A-добавить. P-печать. E-экспорт. I-импорт. F-поиск. D-удалить."
              + "U-изменить. Q-выход")

    def print_notes(self, model: dict):
        for idx, values in model.items():
            print(f'{idx} {values}')
