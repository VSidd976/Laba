from models.system import System
from models.naukma import NaUKMA
# from data2 import csv_mastering


class Faculty(System):
    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)

    def add_instance(self, faculties):
        if self.name not in faculties.dict_of_instance:
            NaUKMA.add_instance_to_dict(self, faculties)
            print(f"Факультет '{self.name}' додано.")
        else:
            print(f"Факультет '{self.name}' вже існує.")
        # csv_mastering.save_data()
    # Додає факультет і її значення в словнику матрьошці

    def delete_instance(self, faculties):
        if self.name not in faculties.dict_of_instance:
            print(f"Факультет '{self.name}' не існує.")
        else:
            del faculties.dict_of_instance[self.name]
            print(f"Факультет '{self.name}' видалено.")
        # csv_mastering.save_data()
    # Видаляє факультет і її ключ зі значенням в словнику матьошці
