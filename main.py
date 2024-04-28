from menu import Menu
from models.csv_mastering import *
get_from_data("C:\\Users\\admin\\Downloads\\laba\\models\\csv_file.txt")
system.add_instance_to_naukma()
people.add_instance_to_naukma()
cathedras.add_instance_to_dict(system)
faculties.add_instance_to_dict(system)
students.add_instance_to_dict(people)
teachers.add_instance_to_dict(people)
# student1 = models.Student("Діма", "Єрмолов",
#                    "Олександрович", "Fi",
#                    "math", "aplied math", "1")
# student1.add_person(students)
# print(students.list_of_instance)
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
    try:
        print(main_menu.display())
        if main_menu.name == "Students":
            command = input("Enter command: Up, Down, Show Info, Edit, Add, Get, Find, Back, Exit ").strip().lower()
        elif main_menu.name == "Teachers":
            command = input("Enter command: Up, Down, Show Info, Edit, Add, Get, Find, Back, Exit ").strip().lower()
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
                specialty = input("Enter specialty: ")
                course = input("Enter course: ")
                cathedra = input("Enter cathedra")
                student = models.Student(name, surname, fathername, faculty, cathedra, specialty, course)
                models.Student.add_person(student, students)
                list_of_student_names.append(f"{student.surname} {student.name} {student.fathername}")
        elif command in ["s", "showinfo"]:
            if main_menu.name == "NaUKMA":
                print("Invalid command")
            elif main_menu.name in ["Students", "Teachers"]:
                student = students.list_of_instance[main_menu.index]
                models.Student.show_info(student, students)

            # Add cathedra teacher and more
        elif command in ["edit"]:
            if main_menu.name == "NaUKMA":
                print("Invalid command")
            elif main_menu.name in ["Students", "Teachers"]:
                student = students.list_of_instance[main_menu.index]
                models.Student.edit_person(student)
                list_of_student_names[main_menu.index] = f"{student.surname} {student.name} {student.fathername}"
        elif command in ["findlistbyfathername"]:
            list_of_fathernames = models.Student.find_list_by_fathername(input("Enter fathername: "), students)
            if list_of_fathernames is None:
                continue
            else:
                for fathername in list_of_fathernames:
                    print(f"Students with this fathername: {fathername.fathername}")

        elif command in ["f", "find"]:
            command2 = input(
                "Введіть за чим хочете шукати [n]ame, "
                "[f]athername, [s]urname, [fa]culty, [c]athedra, [p]ib : ").strip().lower()
            if command2 in ["n", "name"]:
                list_of_names = models.Student.find_list_by_name(input("Enter name: "), students)
                if list_of_names is None:
                    continue
                else:
                    for name in list_of_names:
                        print(f"Students with this name: {name.surname} {name.name} {name.fathername}")
            elif command2 in ["f", "fathername"]:
                list_of_fathernames = models.Student.find_list_by_fathername(input("Enter fathername: "), students)
                if list_of_fathernames is None:
                    continue
                else:
                    for fathername in list_of_fathernames:
                        print(
                            f"Students with this fathername: {fathername.surname} {fathername.name} {fathername.fathername}")
            elif command2 in ["s", "surname"]:
                list_of_surnames = models.Student.find_list_by_surname(input("Enter"), students)
                if list_of_surnames is None:
                    continue
                else:
                    for surname in list_of_surnames:
                        print(f"Students with this fathername: {surname.surname} {surname.name} {surname.fathername}")
            elif command2 in ["fa", "faculty"]:
                list_of_faculties = models.Student.find_list_by_faculty(input("Enter"), students)
                if list_of_faculties is None:
                    continue
                else:
                    for faculty in list_of_faculties:
                        print(f"Students on this faculty: {faculty.surname} {faculty.name} {faculty.fathername}")
            elif command2 in ["c", "cathedra"]:
                list_of_cathedra = models.Student.find_list_by_cathedra(input("Enter cathedra: "), students)
                if list_of_cathedra is None:
                    continue
                else:
                    for cathedra in list_of_cathedra:
                        print(f"Students on this cathedra: {cathedra.surname} {cathedra.name} {cathedra.fathername}")
            elif command2 in ["p", "pib"]:
                list_of_pib = models.Student.find_list_by_pib(input("Enter name: "), input("Enter surname: "),
                                                       input("Enter fathername: "), students)
                if list_of_pib is None:
                    continue
                else:
                    for pib in list_of_pib:
                        print(f"Students with this pib: {pib.surname}{pib.name}{pib.fathername}")
        elif command in ["g", "get"]:
            command2 = input(
                "Введіть за чим хочете шукати [a]lphabet, "
                "alphabet on [f]aculty, [c]ourse, [cc]thedra course : ").strip().lower()
            if command2 in ["a", "alphabet"]:
                sorted_list = models.Student.get_by_alphabet(students)
                for student in sorted_list:
                    print(f"{student.surname} {student.name} {student.fathername}\n")
            elif command2 in ["f", "faculty"]:
                sorted_list = models.Student.get_by_alphabet_on_faculty(input("Enter faculty: "), students)
                if sorted_list is None:
                    print("No students")
                    continue
                for student in sorted_list:
                    print(f"{student.surname} {student.name} {student.fathername}\n")
            elif command2 in ["c", "course"]:
                sorted_list = models.Student.get_by_course(students)
                if sorted_list is None:
                    print("No students")
                    continue
                for student in sorted_list:
                    print(f"{student.surname} {student.name} {student.fathername}\n")
            elif command2 in ["cc", "cathedracourse"]:
                sorted_list = models.Student.get_students_cathedra_course(input("Enter cathedra: "), input("Enter course: "),
                                                                   students)
                if sorted_list is None:
                    print("No students")
                    continue
                for student in sorted_list:
                    print(f"{student.surname} {student.name} {student.fathername}\n")
            else:
                print("Invalid command")
        else:
            print("Invalid command")
    except FileNotFoundError:
        continue
# print(students.list_of_instance[0])
