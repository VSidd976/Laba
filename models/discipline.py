# потім треба замінити всі імпорти на імпорт ініт

from cathedra import *


class Discipline(Cathedra):
    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)

    def add_discipline(self, cathedra):
        # cathedra - кафедра в яку додаємо дисципліну
        if self.name not in cathedra.dict_of_instance:
            NaUKMA.add_instance_to_dict(self, cathedra)
            print(f"Дисципліну '{self.name}' додано.")
        else:
            print(f"Дисципліна '{self.name}' вже існує.")
    # Додає кафедру і її значення в словнику матрьошці

    def delete_discipline(self):
        if self.name not in cathedra.dict_of_instance:
            print(f"Дисципліни '{self.name}' не існує.")
        else:
            del cathedra.dict_of_instance[self.name]
            print(f"Дисципліну '{self.name}' видалено.")
    # Видаляє факультет і її ключ зі значенням в словнику матьошц
