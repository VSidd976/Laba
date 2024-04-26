from person import *
from faculty import *
from cathedra import *


class Teacher(Person):
    def __init__(self, name, surname, fathername, faculty, cathedra):
        super().__init__(name, surname, fathername, faculty)
        self.cathedra = cathedra

    def add_person(self, teacher):
        if self not in teacher.list_of_instance:
            NaUKMA.add_instance_to_list(self, teacher)
            print(f"Викладача '{self.name} {self.surname}' додано.")
        else:
            print(f"Викладача '{self.name} {self.surname}' вже існує.")

    def delete_person(self, teacher):
        if self not in teacher.list_of_instance:
            NaUKMA.add_instance_to_list(self, teacher)
            print(f"Викладача '{self.name} {self.surname}' додано.")
        else:
            print(f"Викладача '{self.name} {self.surname}' вже існує.")

    def edit_person(self):
        answer = input("Впишіть, що ви хочете змінити('n' - ім'я"
                       "'s' - прізвище"
                       "'f' - по-батькові"
                       "'fa' - факультет"
                       "'ca' - кафедра): ")
        if answer == 'n':
            self.name = input("Впишіть відредаговане ім'я викладача: ")
        if answer == 's':
            self.surname = input("Впишіть відредаговане прізвище викладача: ")
        if answer == 'f':
            self.fathername = input("Впишіть відредаговане по-батькові викладача: ")
        if answer == 'fa':
            self.faculty = input("Впишіть відредагований факультет викладача: ")
        if answer == 'ca':
            self.cathedra = input("Впишіть відредаговану групу навчання викладача: ")
        else:
            print("Такої опції не існує")
            pass
        # Дмитре, напишіть тут ще всякі методи щоб виходити назад в меню


kozerenko = Teacher("Serhyi", "Kozerenko", "Oleksandr", fi, math_cathedra)
kundik = Teacher("Kyrylo", "Kundik", "Volodymyr", fi, informatics_cathedra)
NaUKMA.add_instance_to_list(kozerenko, teachers)
NaUKMA.add_instance_to_list(kundik, teachers)


if __name__ == "__main__":
    print(teachers.list_of_instance)
