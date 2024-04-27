from models.person import Person
from models.naukma import NaUKMA


class Student(Person):
    def __init__(self, name, surname, fathername, faculty, specialty, course, group=None):
        super().__init__(name, surname, fathername, faculty)
        self.specialty = specialty
        self.course = course
        self.group = group
        # Тут group за замовчуванням None, бо не на всіх спеціальностях є групи
        # Якщо в студента за пеціальністю є група, то її можна просто вказати, але при тому в студента
        # в якого немає групи не буде проблем з тим, що йому треба заповнювати це поле

    def add_person(self, students):
        if self not in students.list_of_instance:
            NaUKMA.add_instance_to_list(self, students)
            print(f"Студента '{self.name} {self.surname}' додано.")
        else:
            print(f"Студент '{self.name} {self.surname}' вже існує.")

    def delete_person(self, students):
        if self in students.list_of_instance:
            students.list_of_instance.remove(self)
            print(f"Студента '{self.name} {self.surname}' вилучено.")
        else:
            print(f"Студента '{self.name} {self.surname}' не існує.")

    def edit_person(self):
        answer = input("Впишіть, що ви хочете змінити('n' - name \n"
                       "'s' - surname"
                       "'f' - fathername"
                       "'c' - course"
                       "'g' - group): ")
        if answer == 'n':
            self.name = input("Впишіть відредаговане ім'я студента: ")
        if answer == 's':
            self.surname = input("Впишіть відредаговане прізвище студента: ")
        if answer == 'f':
            self.fathername = input("Впишіть відредаговане по-батькові студента: ")
        if answer == 'c':
            self.course = input("Впишіть відредагований курс навчання студента: ")
        if answer == 'g':
            self.group = input("Впишіть відредаговану групу навчання студента: ")
        else:
            print("Такої опції не існує")
            pass
        # Дмитре, напишіть тут ще всякі методи щоб виходити назад в меню
