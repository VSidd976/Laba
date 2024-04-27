from system import *


class Faculty(System):
    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)

    def add_faculty(self, faculty):
        if self.name not in faculty.dict_of_instance:
            NaUKMA.add_instance_to_dict(self, faculty)
            print(f"Факультет '{self.name}' додано.")
        else:
            print(f"Факультет '{self.name}' вже існує.")
    # Додає факультет і її значення в словнику матрьошці

    def delete_faculty(self, faculty):
        if self.name not in faculty.dict_of_instance:
            print(f"Факультет '{self.name}' не існує.")
        else:
            del faculty.dict_of_instance[self.name]
            print(f"Факультет '{self.name}' видалено.")
    # Видаляє факультет і її ключ зі значенням в словнику матьошці

    def edit_faculty(self):
        answer = input("Впишіть, що ви хочете змінити('n' - name \n"
                       "'f' - field of study: ")
        if answer == 'n':
            self.name = input("Впишіть відредаговану назву кафедри: ")
        if answer == 'f':
            self.field_of_study = input("Впишіть відредагований предмет вивчення: ")
        else:
            print("Такої опції не існує")
            pass
        # Дмитре Раяне Гослінгу, напишіть тут ще всякі методи щоб виходити назад в меню

fi = Faculty('FI', "Informatics")
fen = Faculty('FEN', "Economy")
# NaUKMA.add_instance_to_dict(fi, faculties)
# NaUKMA.add_instance_to_dict(fen, faculties)
fi.add_faculty(faculties)
fen.add_faculty(faculties)
fi.delete_faculty(faculties)
fen.delete_faculty(faculties)


if __name__ == "__main__":
    print(faculties.dict_of_instance)
