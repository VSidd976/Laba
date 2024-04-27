from system import *


class Cathedra(System):
    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)

    def add_cathedra(self, cathedra):
        if self.name not in cathedra.dict_of_instance:
            NaUKMA.add_instance_to_dict(self, cathedra)
            print(f"Кафедра '{self.name}' додано.")
        else:
            print(f"Кафедра '{self.name}' вже існує.")
    # Додає кафедру і її значення в словнику матрьошці

    def delete_cathedra(self, cathedra):
        if self.name not in cathedra.dict_of_instance:
            print(f"Кафедри '{self.name}' не існує.")
        else:
            del cathedra.dict_of_instance[self.name]
            print(f"Кафедру '{self.name}' видалено.")
    # Видаляє кафедру і її ключ зі значенням в словнику матьошці

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


math_cathedra = Cathedra("Math", "All that connected to math")
economy_cathedra = Cathedra("Economy", "All that connected to economy")
informatics_cathedra = Cathedra("Informatics", "All that connected to informatics")
# NaUKMA.add_instance_to_dict(math_cathedra, cathedras)
# NaUKMA.add_instance_to_dict(economy_cathedra, cathedras)
# NaUKMA.add_instance_to_dict(informatics_cathedra, cathedras)


if __name__ == "__main__":
    math_cathedra.add_cathedra(cathedras)
    economy_cathedra.add_cathedra(cathedras)
    informatics_cathedra.add_cathedra(cathedras)
    math_cathedra.delete_cathedra(cathedras)
    economy_cathedra.delete_cathedra(cathedras)
    informatics_cathedra.delete_cathedra(cathedras)
    print(cathedras.dict_of_instance)
