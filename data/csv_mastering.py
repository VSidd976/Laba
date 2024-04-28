import csv
import models


students = models.Person("Students")
teachers = models.Person("Teachers")
faculties = models.System("Faculties")
cathedras = models.System("Cathedras")
student = models.Student("Dima", "S", "Email", "Phone", "Adress", "1")
student_2 = models.Student("Valik", "V", "Gmail", "one", "dress", "4")
teacher = models.Teacher("Dimon", "Kozerenko", "A", "YO", "MAth")
student.add_person(students)
student_2.add_person(students)
teacher.add_person(teachers)
students_list = [[i.name, i.surname, i.fathername, i.faculty, i.specialty, i.course]
                 for i in students.list_of_instance]
teachers_list = [[i.name, i.surname, i.fathername, i.faculty, i.cathedra]
                 for i in teachers.list_of_instance]
faculties_list = [[i.name, i.field_of_study]
                  for i in faculties.list_of_instance]
cathedras_list = [[i.name. i.cathedra]
                  for i in cathedras.list_of_instance]

print(students_list)
print(teachers_list)


def save_data():
    with open('C:\\Users\\admin\\Downloads\\laba\\data\\csv_file', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Students data:"])
        writer.writerow(['Name', 'Surname', 'Fathername', 'Faculty', 'Specialty', 'Course'])
        for row in students_list:
            writer.writerow(row)
        writer.writerow(["Teachers data:"])
        writer.writerow(['Name', 'Surname', 'Fathername', 'Faculty', 'Cathedra'])
        for row in teachers_list:
            writer.writerow(row)
        writer.writerow(["Faculties data:"])
        writer.writerow(['Name', 'Field of study'])
        for row in faculties_list:
            writer.writerow(row)
        writer.writerow(["Cathedras data:"])
        writer.writerow(['Name', 'Field of study'])
        for row in cathedras_list:
            writer.writerow(row)
# Зберегти дані програми в локальне сховище.


def read_from_data():
    with open('C:\\Users\\admin\\Downloads\\laba\\data\\csv_file', 'r', newline='', encoding='utf-8') as file:
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
            if not row:
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
                name, surname, fathername, faculty, specialty, course = row
                student1 = models.Student(name, surname, fathername, faculty, specialty, course)
                student1.add_person(students)
            elif current_section == "teachers":
                name, surname, fathername, faculty, cathedra = row
                teacher1 = models.Teacher(name, surname, fathername, faculty, cathedra)
                teacher1.add_person(teachers)
            elif current_section == "faculties":
                name, field_of_study = row
                faculty = models.Faculty(name, field_of_study)
                faculties.add_instance(faculty)
            elif current_section == "cathedras":
                name, cathedra = row
                cathedra_instance = models.Cathedra(name, cathedra)
                cathedras.add_instance(cathedra_instance)
# Відновити дані з локального сховища
