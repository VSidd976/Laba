from faculty import *


class Specialty(Faculty):
    def __init__(self, name, field_of_study, id_number: int):
        super().__init__(name, field_of_study)
        self.id_number = id_number

    def add_speciality(self, speciality):
        if self.name not in speciality.dict_of_instance:
            NaUKMA.add_instance_to_dict(self, speciality)
            print(f"Спеціальність '{self.name}' додано.")
        else:
            print(f"Спеціальність '{self.name}' вже існує.")
    # Додає спеціальність і її значення в словнику матрьошці

    def delete_speciality(self, speciality):
        if self.name not in speciality.dict_of_instance:
            print(f"Спеціальності '{self.name}' не існує.")
        else:
            del speciality.dict_of_instance[self.name]
            print(f"Спеціальність '{self.name}' видалено.")


am = Specialty("Applied Mathematics", "Applied use of math", 113)
se = Specialty("Software Engineering", "Programing", 121)
NaUKMA.add_instance_to_list(am, fi)
NaUKMA.add_instance_to_list(se, fi)


if __name__ == "__main__":
    print(fi.list_of_instance)
