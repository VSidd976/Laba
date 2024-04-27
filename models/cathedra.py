from models.system import System
from models.naukma import NaUKMA


class Cathedra(System):
    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)

    def add_cathedra(self, cathedras):
        if self.name not in cathedras.dict_of_instance:
            NaUKMA.add_instance_to_dict(self, cathedras)
            print(f"Кафедра '{self.name}' додано.")
        else:
            print(f"Кафедра '{self.name}' вже існує.")
    # Додає кафедру і її значення в словнику матрьошці

    def delete_cathedra(self, cathedras):
        if self.name not in cathedras.dict_of_instance:
            print(f"Кафедри '{self.name}' не існує.")
        else:
            del cathedras.dict_of_instance[self.name]
            print(f"Кафедру '{self.name}' видалено.")
    # Видаляє кафедру і її ключ зі значенням в словнику матьошці
