import errors
from models.system import System
from models.csv_mastering import save_data


class Cathedra(System):
    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)

    def add_instance(self, cathedras):
        if self not in cathedras.list_of_instance:
            cathedras.list_of_instance.append(self)
        else:
            raise errors.ItemExistsError(f"Кафедра '{self.name}' вже існує.")
        save_data()
    # Додає кафедру і її значення в словнику матрьошці

    def delete_instance(self, cathedras):
        if self not in cathedras.list_of_instance:
            raise errors.ItemNotFoundError(f"Кафедри '{self.name}' не існує.")
        else:
            cathedras.list_of_instance.remove(self)
            print(f"Кафедру '{self.name}' видалено.")
        save_data()
    # Видаляє кафедру і її ключ зі значенням в словнику матьошці

    def edit_system_instance(self):
        new_field = input("Впишіть нову сферу "
                          "вивчення(якщо хочете залишити минулу,"
                          " впишіть '-'):")
        if new_field == '-':
            pass
        else:
            self.field_of_study = new_field
        save_data()
