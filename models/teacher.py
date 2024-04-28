from models.person import Person
from models.naukma import NaUKMA
# from data import csv_mastering


alphabet = ["А", "Б", "В", "Г", "Ґ", "Д", "Е", "Є", "Ж", "З", "И", "І", "Ї", "Й",
            "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч",
            "Ш", "Щ", "Ь", "Ю", "Я"]
# потім прибрати алфавіт


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
        # csv_mastering.save_data()

    def delete_person(self, teacher):
        if self not in teacher.list_of_instance:
            NaUKMA.add_instance_to_list(self, teacher)
            print(f"Викладача '{self.name} {self.surname}' додано.")
        else:
            print(f"Викладача '{self.name} {self.surname}' вже існує.")
        # csv_mastering.save_data()

    def show_info(self, teachers):
        if self not in teachers.list_of_instance:
            print("Викладача не існує.")
        else:
            print(f"Інформація про викладача:\n"
                  f"Ім'я: {self.name}\n"
                  f"Прізвище: {self.surname}\n"
                  f"Факультет: {self.faculty}\n"
                  f"Кафедра: {self.cathedra}\n")

    @staticmethod
    def find_list_by_name(name, teachers):
        list_by_name = []
        counter = 0
        for teacher in teachers.list_of_instance:
            if teacher.name == name:
                list_by_name.append(teacher)
                counter += 1
        if counter == 0:
            print(f"Викладачів з іменем {name} не існує")
            return None
        else:
            return list_by_name

    @staticmethod
    def find_list_by_surname(surname, teachers):
        list_by_surname = []
        counter = 0
        for teacher in teachers.list_of_instance:
            if teacher.surname == surname:
                list_by_surname.append(teacher)
                counter += 1
        if counter == 0:
            print(f"Викладачів з прізвищем {surname} не існує")
            return None
        else:
            return list_by_surname

    @staticmethod
    def find_list_by_fathername(fathername, teachers):
        list_by_fathername = []
        counter = 0
        for teacher in teachers.list_of_instance:
            if teacher.fathername == fathername:
                list_by_fathername.append(teacher)
                counter += 1
        if counter == 0:
            print(f"Викладачів з по-батькові {fathername} не існує")
            return None
        else:
            return list_by_fathername

    @staticmethod
    def find_list_by_pib(name, surname, fathername, teachers):
        list_by_pib = []
        counter = 0
        for teacher in teachers.list_of_instance:
            if (teacher.name == name
                    and teacher.surname == surname
                    and teacher.fathername == fathername):
                list_by_pib.append(teacher)
                counter += 1
        if counter == 0:
            print(f"Викладачів з таким ПІБ не існує")
            return None
        else:
            return list_by_pib

    @staticmethod
    def get_by_alphabet(teacher):
        list_by_alphabet = []
        list_of_teacher = teacher.list_of_instance
        for letter in alphabet:
            for i in list_of_teacher:
                if letter == i.surname[0]:
                    list_by_alphabet.append(list_of_teacher[i])
        return list_by_alphabet

    # Вивести інформацію про всіх студентів факультета впорядкованих за алфавітом.

    @staticmethod
    def find_list_by_faculty(faculty, teacher):
        list_by_faculty = []
        counter = 0
        for teach in teacher.list_of_instance:
            if teach.faculty == faculty:
                list_by_faculty.append(teach)
                counter += 1
        if counter == 0:
            print(f"Викладачів в {faculty} факультеті не існує")
            return None
        else:
            return list_by_faculty

    @staticmethod
    def find_list_by_cathedra(cathedra, teacher):
        list_by_cathedra = []
        counter = 0
        for teach in teacher.list_of_instance:
            if teach.cathedra == cathedra:
                list_by_cathedra.append(teach)
                counter += 1
        if counter == 0:
            print(f"Викладачів в {cathedra} кафедрі не існує")
            return None
        else:
            return list_by_cathedra

    @staticmethod
    def get_by_alphabet_on_faculty(faculty, teacher):
        list_by_alphabet = []
        list_by_faculty = Teacher.find_list_by_faculty(faculty, teacher)
        for letter in alphabet:
            for i in list_by_faculty:
                if letter == i.surname[0]:
                    list_by_alphabet.append(list_by_faculty[i])
        return list_by_alphabet
    # Вивести інформацію про всіх викладачів факультета впорядкованих за алфавітом.

    @staticmethod
    def get_by_cathedra_by_alphabet(cathedra, teacher):
        sorted_list = []
        list_by_alphabet = Teacher.get_by_alphabet(teacher)
        list_by_cathedra = Teacher.find_list_by_cathedra(cathedra, teacher)
        for teach in list_by_cathedra:
            for teach_2 in list_by_alphabet:
                if teach == teach_2:
                    sorted_list.append(teach)
        return sorted_list
    # Вивести інформацію про всіх студентів кафедри впорядкованих за алфавітом.

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
        # csv_mastering.save_data()
        # Дмитре, напишіть тут ще всякі методи щоб виходити назад в меню
