from note import Note
file_path="notes.csv"
def write_file(file_path,array, mode):
    file = open(file_path, mode=mode, encoding='utf-8')
    file.seek(0)
    file.close()
    file = open(file_path, mode=mode, encoding='utf-8')
    for notes in array:
        file.write(note.Note.to_string(notes))
        file.write('\n')
    file.close


def read_file(file_path):
    try:
        array = []
        with open(file_path, "r", encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                split_line = line.strip().split(";")
                if len(split_line) == 4:  # Проверяем, что строка разделяется на 4 элемента
                    note = Note(id=split_line[0], title=split_line[1], body=split_line[2], date=split_line[3])
                    array.append(note)
                else:
                    print(f"Неправильный формат строки: {line}")
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
    return array