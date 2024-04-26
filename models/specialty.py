from faculty import *


class Specialty(Faculty):
    def __init__(self, name, field_of_study, id_number: int):
        super().__init__(name, field_of_study)
        self.id_number = id_number


am = Specialty("Applied Mathematics", "Applied use of math", 113)
se = Specialty("Software Engineering", "Programing", 121)
NaUKMA.add_instance_to_list(am, fi)
NaUKMA.add_instance_to_list(se, fi)


if __name__ == "__main__":
    print(fi.list_of_instance)
