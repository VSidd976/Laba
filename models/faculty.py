from models.system import System
from models.csv_mastering import save_data
import errors


class Faculty(System):
    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)

    def add_instance(self, faculties):
        if self not in faculties.list_of_instance:
            faculties.list_of_instance.append(self)
        else:
            raise errors.ItemExistsError(f"Факультет '{self.name}' вже існує.")
        save_data()
    # Додає факультет і її значення в словнику матрьошці

    def delete_instance(self, faculties):
        if self not in faculties.list_of_instance:
            raise errors.ItemNotFoundError(f"Факультет '{self.name}' не існує.")
        else:
            faculties.list_of_instance.remove(self)
            print(f"Факультет '{self.name}' видалено.")
            save_data()
    # Видаляє факультет і її ключ зі значенням в словнику матьошці

    def edit_system_instance(self):
        new_field = input("Впишіть нову сферу "
                          "вивчення(якщо хочете залишити минулу,"
                          " впишіть '-'):")
        if new_field == '-':
            pass
        else:
            self.field_of_study = new_field
        save_data()
