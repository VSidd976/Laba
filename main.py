import models
from menu import Menu

# from data import csv_mastering


system = models.NaUKMA("System")
people = models.NaUKMA("People")
cathedras = models.System("Cathedras")
faculties = models.System("Faculties")
students = models.Person("Students")
teachers = models.Person("Teachers")
system.add_instance_to_naukma()
people.add_instance_to_naukma()
cathedras.add_instance_to_dict(system)
faculties.add_instance_to_dict(system)
students.add_instance_to_dict(people)
teachers.add_instance_to_dict(people)
student1 = models.Student("name", "surname",
                          "fathername", "faculty",
                          "speciality", "course")
student1.add_person(students)

if __name__ == "__main__":

    list_of_student_names = []
    for student in students.list_of_instance:
        list_of_student_names.append(f"{student.surname} {student.name} {student.fathername}")
    list_of_teacher_names = []
    for teacher in teachers.list_of_instance:
        list_of_teacher_names.append(f"{teacher.surname} {teacher.name} {teacher.fathername}")
    menu1 = Menu("NaUKMA", list(models.NaUKMA.dict_of_naukma.keys()))
    menu2 = Menu("People", list(people.dict_of_instance.keys()))
    menu3 = Menu("System", list(system.dict_of_instance.keys()))
    menu4 = Menu("Cathedras", list(cathedras.dict_of_instance.keys()))
    menu5 = Menu("Faculties", list(faculties.dict_of_instance.keys()))
    menu6 = Menu("Students", list_of_student_names)
    menu7 = Menu("Teachers", list_of_teacher_names)
    menu_dict = {"NaUKMA": menu1, "People": menu2,
                 "System": menu3, "Cathedras": menu4,
                 "Faculties": menu5, "Students": menu6,
                 "Teachers": menu7}
    menu_dict2 = {"People": menu1, "System": menu1, "Cathedras": menu3,
                  "Faculties": menu3, "Students": menu2, "Teachers": menu2}
    main_menu = menu1

    while True:
        print(main_menu.display())
        if (main_menu.name == "Faculties" or main_menu.name == "Lecturers"
                or main_menu.name == "Students" or main_menu.name == "Cathedras"):
            command = input("Enter command: Up Down GetInfo Back Exit ").strip().lower()
        else:
            command = input("Enter command: Up Down Open Back Exit ").strip().lower()
        if command in ["u", "up"]:
            main_menu.up()
        elif command in ["d", "down"]:
            main_menu.down()
        elif command in ["o", "open"]:
            main_menu = menu_dict[main_menu.content[main_menu.index]]
        elif command in ["b", "back"]:
            main_menu = menu_dict2[main_menu.name]
        elif command in ["exit"]:
            break
        elif command in ["a", "add"]:
            if main_menu.name == "NaUKMA":
                print("Invalid command")
            elif main_menu.name in ["Students", "Teachers"]:
                name = input("Enter name: ")
                surname = input("Enter surname: ")
                fathername = input("Enter fathername: ")
                faculty = input("Enter faculty: ")
                speciality = input("Enter speciality: ")
                course = input("Enter course: ")
                student = models.Student(name, surname, fathername, faculty, speciality, course)
                models.Student.add_person(student, students)
                list_of_student_names.append(f"{student.surname} {student.name} {student.fathername}")
        elif command in ["s", "showinfo"]:
            if main_menu.name == "NaUKMA":
                print("Invalid command")
            elif main_menu.name in ["Students", "Teachers"]:
                student = students.list_of_instance[main_menu.index]
                student.show_info(students)

            # Add cathedra teacher and more
        elif command in ["edit"]:
            if main_menu.name == "NaUKMA":
                print("Invalid command")
            elif main_menu.name in ["Students", "Teachers"]:
                student = students.list_of_instance[main_menu.index]
                student.edit_person()
                list_of_student_names[main_menu.index] = f"{student.surname} {student.name} {student.fathername}"
        elif command in ["findlistbyfathername"]:
            print(models.Student.find_list_by_fathername(input("fathername"), students))

        else:
            print("Invalid command")
    # print(students.list_of_instance[0])
