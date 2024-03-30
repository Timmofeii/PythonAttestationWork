from note import Note 
class UI:
    def create_note(number):
        title =  input('Введите Название заметки: ')
        body = input('Введите Описание заметки: ')
        return Note(title=title, body=body)


    def main_menu() -> int:
        main_menu_choice = 'Выберите пункт меню: '
        main_menu=["Это программа 'Заметки'. Имеются следующие функции:",
                   "Вывод всех заметок из файла",
                   "Добавление заметки",
                   "Удаление заметки",
                   "Редактирование заметки",
                   "Выборка заметок по дате",
                   "Показать заметку по id",
                   "Выход "]
        for index, item in enumerate(main_menu):
            if index == 0:
                print(item)
            else:
                print(f'\t{index}. {item}')
        while True:
            choice = input(main_menu_choice)
            if choice.isdigit() and 0 < int(choice) < len(main_menu):
                return int(choice)

    
    def check(self):
        print("check")
    def exit():
        print("До свидания!")