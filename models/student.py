from models.person import Person
from models.naukma import NaUKMA
alphabet = ["А", "Б", "В", "Г", "Ґ", "Д", "Е", "Є", "Ж", "З", "И", "І", "Ї", "Й",
            "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч",
            "Ш", "Щ", "Ь", "Ю", "Я"]
# потім прибрати алфавіт


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

    def show_info(self, students):
        if self not in students.list_of_instance:
            print("Студента не існує.")
        else:
            print(f"Інформація про студента:\n"
                  f"Ім'я: {self.name}\n"
                  f"Прізвище: {self.surname}\n"
                  f"Факультет: {self.faculty}\n"
                  f"Спеціальність: {self.specialty}\n"
                  f"Курс: {self.course}\n")
            if self.group is not None:
                print(f"Група: {self.group}")
    # Виводить всю інформацію про студента

    @staticmethod
    def find_list_by_name(name, students):
        list_by_name = []
        counter = 0
        for student in students.list_of_instance:
            if student.name == name:
                list_by_name.append(student)
                counter += 1
        if counter == 0:
            print(f"Студентів з іменем {name} не існує")
            return None
        else:
            return list_by_name

    @staticmethod
    def find_list_by_surname(surname, students):
        list_by_surname = []
        counter = 0
        for student in students.list_of_instance:
            if student.surname == surname:
                list_by_surname.append(student)
                counter += 1
        if counter == 0:
            print(f"Студентів з прізвищем {surname} не існує")
            return None
        else:
            return list_by_surname

    @staticmethod
    def find_list_by_fathername(fathername, students):
        list_by_fathername = []
        counter = 0
        for student in students.list_of_instance:
            if student.fathername == fathername:
                list_by_fathername.append(student)
                counter += 1
        if counter == 0:
            print(f"Студентів з по-батькові {fathername} не існує")
            return None
        else:
            print(f"{fathername} with this fathername {list_by_fathername}")
            return list_by_fathername

    @staticmethod
    def find_list_by_pib(name, surname, fathername, students):
        list_by_pib = []
        counter = 0
        for student in students.list_of_instance:
            if (student.name == name
                    and student.surname == surname
                    and student.fathername == fathername):
                list_by_pib.append(student)
                counter += 1
        if counter == 0:
            print(f"Студентів з таким ПІБ не існує")
            return None
        else:
            return list_by_pib

    @staticmethod
    def find_list_by_course(course, students):
        list_by_course = []
        counter = 0
        for student in students.list_of_instance:
            if student.course == course:
                list_by_course.append(student)
                counter += 1
        if counter == 0:
            print(f"Студентів на {course}-му курсі не існує")
            return None
        else:
            return list_by_course

    @staticmethod
    def find_list_by_group(group, students):
        list_by_group = []
        counter = 0
        for student in students.list_of_instance:
            if student.group == group:
                list_by_group.append(student)
                counter += 1
        if counter == 0:
            print(f"Студентів в {group}-ій групі не існує")
            return None
        else:
            return list_by_group

    @staticmethod
    def find_list_by_faculty(faculty, students):
        list_by_faculty = []
        counter = 0
        for student in students.list_of_instance:
            if student.faculty == faculty:
                list_by_faculty.append(student)
                counter += 1
        if counter == 0:
            print(f"Студентів в {faculty} факультеті не існує")
            return None
        else:
            return list_by_faculty

    @staticmethod
    def find_list_by_cathedra(cathedra, students):
        list_by_cathedra = []
        counter = 0
        for student in students.list_of_instance:
            if student.cathedra == cathedra:
                list_by_cathedra.append(student)
                counter += 1
        if counter == 0:
            print(f"Студентів в {cathedra} кафедрі не існує")
            return None
        else:
            return list_by_cathedra
    # Методи вище перевіряють чи існують студенти які відповідають певним параметром
    # і повертають лісти з якимись параметрами, після них в меню треба буде прописати
    # вибір людини і використати метод show_info
    # Ще тут треба пофіксити списки

    @staticmethod
    def get_by_alphabet(students):
        list_by_alphabet = []
        list_of_students = students.list_of_instance
        for letter in alphabet:
            for i in list_of_students:
                if letter == i.surname[0]:
                    list_by_alphabet.append(list_of_students[i])
        return list_by_alphabet
    # Вивести інформацію про всіх студентів факультета впорядкованих за алфавітом.

    @staticmethod
    def get_by_alphabet_on_faculty(faculty, students):
        list_by_alphabet = []
        list_by_faculty = Student.find_list_by_faculty(faculty, students)
        for letter in alphabet:
            for i in list_by_faculty:
                if letter == i.surname[0]:
                    list_by_alphabet.append(list_by_faculty[i])
        return list_by_alphabet
    # Вивести інформацію про всіх студентів факультета впорядкованих за алфавітом.

    @staticmethod
    def get_by_course(student):
        list_by_course = []
        list_of_students = student.list_of_instance
        for i in [1, 2, 3, 4, 5, 6]:
            for j in list_of_students:
                if i == j.course:
                    list_by_course.append(j)
        return list_by_course
    # Вивести інформацію про всіх студентів впорядкованих за курсами.

    @staticmethod
    def get_by_cathedra_s_course(cathedra, students):
        sorted_list = []
        list_by_course = Student.get_by_course(students)
        list_by_cathedra = Student.find_list_by_cathedra(cathedra, students)
        for student in list_by_cathedra:
            for student_2 in list_by_course:
                if student == student_2:
                    sorted_list.append(student)
        return sorted_list
    # Вивести інформацію про всіх студентів кафедри впорядкованих за курсами.

    @staticmethod
    def get_by_cathedra_by_alphabet(cathedra, students):
        sorted_list = []
        list_by_alphabet = Student.get_by_alphabet(students)
        list_by_cathedra = Student.find_list_by_cathedra(cathedra, students)
        for student in list_by_cathedra:
            for student_2 in list_by_alphabet:
                if student == student_2:
                    sorted_list.append(student)
        return sorted_list
    # Вивести інформацію про всіх студентів кафедри впорядкованих за алфавітом.

    @staticmethod
    def get_students_cathedra_course(cathedra, course, students):
        list_by_course = Student.find_list_by_course(course, students)
        list_by_cathedra = Student.find_list_by_cathedra(cathedra, students)
        sorted_list = []
        for student in list_by_course:
            for student_2 in list_by_cathedra:
                if student == student_2:
                    sorted_list.append(student)
        return sorted_list
    # Вивести інформацію про всіх студентів кафедри вказаного курсу.

    @staticmethod
    def get_students_course_cathedra_alphabet(course, cathedra, students):
        list_cathedra_course = Student.get_students_cathedra_course(cathedra, course, students)
        sorted_list = []
        for letter in alphabet:
            for student in list_cathedra_course:
                if student.surname[0] == letter:
                    sorted_list.append(student)
        return sorted_list
    # Вивести інформацію про всіх студентів кафедри вказаного курсу впорядкованих за алфавітом.
    # Всі методи зверху повертають потрібний відсортований список

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
    # Дмитре Раяне Гослінгу, напишіть тут ще всякі методи щоб виходити назад в меню
