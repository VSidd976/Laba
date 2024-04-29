import csv
from models.objects import *


def data_clean():
    with open("models\\csv_file.txt", 'w', newline='', encoding='utf-8'):
        pass


def save_data():
    data_clean()
    students_list = [[i.name, i.surname, i.fathername, i.faculty, i.cathedra, i.specialty, i.course]
                     for i in students.list_of_instance]
    teachers_list = [[i.name, i.surname, i.fathername, i.faculty, i.cathedra]
                     for i in teachers.list_of_instance]
    faculties_list = [[i.name, i.field_of_study]
                      for i in faculties.list_of_instance]
    cathedras_list = [[i.name, i.field_of_study]
                      for i in cathedras.list_of_instance]
    with open("models\\csv_file.txt", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Students data:"])
        # Формат: 'Name', 'Surname', 'Fathername', 'Faculty', 'Cathedra', 'Specialty', 'Course'
        for row in students_list:
            writer.writerow(row)
        writer.writerow(["Teachers data:"])
        # Формат: 'Name', 'Surname', 'Fathername', 'Faculty', 'Cathedra'
        for row in teachers_list:
            writer.writerow(row)
        writer.writerow(["Faculties data:"])
        # Формат: 'Name', 'Field of study'
        for row in faculties_list:
            writer.writerow(row)
        writer.writerow(["Cathedras data:"])
        # Формат: 'Name', 'Field of study'
        for row in cathedras_list:
            writer.writerow(row)
# Зберегти дані програми в локальне сховище.


def read_from_data():
    with open('models\\csv_file.txt', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            result_string = ", ".join(row)
            print(result_string)
# Прочитати дані програми з локального сховища.


def get_from_data(input_file_direction):
    with open(input_file_direction, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        current_section = None
        for row in reader:
            if not row or row == '':
                continue
            if "Students data:" in row:
                current_section = "students"
                continue
            elif "Teachers data:" in row:
                current_section = "teachers"
                continue
            elif "Faculties data:" in row:
                current_section = "faculties"
                continue
            elif "Cathedras data:" in row:
                current_section = "cathedras"
                continue
            if current_section == "students":
                name, surname, fathername, faculty, cathedra, speciality, course = row
                student1 = models.Student(name, surname, fathername, faculty, cathedra, speciality, course)
                student1.add_person(students)
            elif current_section == "teachers":
                name, surname, fathername, faculty, cathedra = row
                teacher1 = models.Teacher(name, surname, fathername, faculty, cathedra)
                teacher1.add_person(teachers)
            elif current_section == "faculties":
                name, field_of_study = row
                faculty1 = models.Faculty(name, field_of_study)
                faculty1.add_instance(faculties)
            elif current_section == "cathedras":
                name, field_of_study = row
                cathedra1 = models.Cathedra(name, field_of_study)
                cathedra1.add_instance(cathedras)
    save_data()
# Відновити дані з локального сховища
