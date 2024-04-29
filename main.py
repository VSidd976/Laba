import errors
from menu import Menu
from models.csv_mastering import *
system.add_instance_to_naukma()
people.add_instance_to_naukma()
cathedras.add_instance_to_dict(system)
faculties.add_instance_to_dict(system)
students.add_instance_to_dict(people)
teachers.add_instance_to_dict(people)
get_from_data("models\\csv_file.txt")
list_of_student_names = []
for student in students.list_of_instance:
    list_of_student_names.append(f"{student.surname} {student.name} {student.fathername}")
list_of_teacher_names = []
for teacher in teachers.list_of_instance:
    list_of_teacher_names.append(f"{teacher.surname} {teacher.name} {teacher.fathername}")
list_of_faculty_names = []
for faculty in faculties.list_of_instance:
    list_of_faculty_names.append(f"{faculty.name}")
list_of_cathedra_names = []
for cathedra in cathedras.list_of_instance:
    list_of_cathedra_names.append(f"{cathedra.name}")
menu1 = Menu("NaUKMA", list(models.NaUKMA.dict_of_naukma.keys()))
menu2 = Menu("People", list(people.dict_of_instance.keys()))
menu3 = Menu("System", list(system.dict_of_instance.keys()))
menu4 = Menu("Cathedras", list_of_cathedra_names)
menu5 = Menu("Faculties", list_of_faculty_names)
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
        if main_menu.name in ["Students", "Teachers"]:
            command = input("Enter command: [U]p, [D]own, [S]how Info, "
                            "[E]dit, [A]dd, [Del]ete [G]et, [F]ind, [B]ack, E[x]it >>> ").strip().lower()
        elif main_menu.name in ["Faculties", "Cathedras"]:
            command = input("Enter command: [U]p, [D]own, [E]dit, [A]dd, [Del]ete [B]ack, E[x]it >>> ").strip().lower()
        else:
            command = input("Enter command: [U]p [D]own [O]pen [B]ack E[x]it >>> ").strip().lower()
        if command in ["u", "up"]:
            main_menu.up()
        elif command in ["d", "down"]:
            main_menu.down()
        elif command in ["o", "open"]:
            main_menu = menu_dict[main_menu.content[main_menu.index]]
        elif command in ["b", "back"]:
            if main_menu.name == "NaUKMA":
                print("Invalid command")
            else:
                main_menu = menu_dict2[main_menu.name]
        elif command in ["x", "exit"]:
            break
        elif main_menu.name == "Students":
            if command in ["s", "showinfo"]:
                student = students.list_of_instance[main_menu.index]
                models.Student.show_info(student, students)
            elif command in ["del", "delete"]:
                student = students.list_of_instance[main_menu.index]
                list_of_student_names.remove(f"{student.surname} {student.name} {student.fathername}")
                models.Student.delete_person(student, students)
            elif command in ["a", "add"]:
                name = input("Введіть ім'я: ")
                surname = input("Введіть прізвище: ")
                fathername = input("Введіть по-батькові: ")
                faculty = input("Введіть факультет: ")
                specialty = input("Введіть спеціальність: ")
                course = input("Введіть курс: ")
                cathedra = input("Введіть кафедру: ")
                student = models.Student(name, surname, fathername, faculty, cathedra, specialty, course)
                models.Student.add_person(student, students)
                list_of_student_names.append(f"{student.surname} {student.name} {student.fathername}")
                # Add cathedra teacher and more
            elif command in ["e", "edit"]:
                student = students.list_of_instance[main_menu.index]
                models.Student.edit_person(student)
                list_of_student_names[main_menu.index] = f"{student.surname} {student.name} {student.fathername}"
    
            elif command in ["f", "find"]:
                command2 = input(
                    "Введіть за чим хочете шукати: [n]ame, "
                    "[f]athername, [s]urname, [fa]culty, [c]athedra, [p]ib >>> ").strip().lower()
                if command2 in ["n", "name"]:
                    list_of_names = models.Student.find_list_by_name(input("Введіть ім'я: "), students)
                    if list_of_names is None:
                        continue
                    else:
                        for name in list_of_names:
                            print(f"Студенти з цим ім'ям: {name.surname} {name.name} {name.fathername}")
                            models.Student.show_info(name, students)
                elif command2 in ["f", "fathername"]:
                    list_of_fathernames = models.Student.find_list_by_fathername(input("Введіть по-батькові: "),
                                                                                 students)
                    if list_of_fathernames is None:
                        continue
                    else:
                        for fathername in list_of_fathernames:
                            print(f"Студенти з цим по-батькові:"
                                  f" {fathername.surname} {fathername.name} {fathername.fathername}")
                            models.Student.show_info(fathername, students)
                elif command2 in ["s", "surname"]:
                    list_of_surnames = models.Student.find_list_by_surname(input("Введіть прізвище: "), students)
                    if list_of_surnames is None:
                        continue
                    else:
                        for surname in list_of_surnames:
                            print(f"Студенти з цим прізвищем: {surname.surname} {surname.name} {surname.fathername}")
                            models.Student.show_info(surname, students)
                elif command2 in ["fa", "faculty"]:
                    list_of_faculties = models.Student.find_list_by_faculty(input("Введіть факультет: "), students)
                    if list_of_faculties is None:
                        continue
                    else:
                        for faculty in list_of_faculties:
                            print(f"Студенти цього факультету: {faculty.surname} {faculty.name} {faculty.fathername}")
                            models.Student.show_info(faculty, students)
                elif command2 in ["c", "cathedra"]:
                    list_of_cathedra = models.Student.find_list_by_cathedra(input("Введіть кафедру: "), students)
                    if list_of_cathedra is None:
                        continue
                    else:
                        for cathedra in list_of_cathedra:
                            print(f"Студенти на цій кафедрі: {cathedra.surname} {cathedra.name} {cathedra.fathername}")
                            models.Student.show_info(cathedra, students)
                elif command2 in ["p", "pib"]:
                    list_of_pib = models.Student.find_list_by_pib(input("Введіть ім'я: "), input("Введіть прізвище: "),
                                                                  input("Введіть по-батькові: "), students)
                    if list_of_pib is None:
                        continue
                    else:
                        for pib in list_of_pib:
                            print(f"Студенти з цим ПІБ: {pib.surname}{pib.name}{pib.fathername}")
                            models.Student.show_info(pib, students)
            elif command in ["g", "get"]:
                command2 = input(
                    "Введіть за чим хочете шукати [a]lphabet, "
                    "alphabet on [f]aculty, [c]ourse, [cc]thedra course : ").strip().lower()
                if command2 in ["a", "alphabet"]:
                    sorted_list = models.Student.get_by_alphabet(students)
                    for student in sorted_list:
                        print(f"{student.surname} {student.name} {student.fathername}\n")
                elif command2 in ["f", "faculty"]:
                    sorted_list = models.Student.get_by_alphabet_on_faculty(input("Введіть факультет: "), students)
                    if sorted_list is None:
                        print("Немає студентів на цьому факультеті")
                        continue
                    for student in sorted_list:
                        print(f"{student.surname} {student.name} {student.fathername}\n")
                elif command2 in ["c", "course"]:
                    sorted_list = models.Student.get_by_course(students)
                    if sorted_list is None:
                        print("Немає студенів на цьому курсі")
                        continue
                    for student in sorted_list:
                        print(f"{student.surname} {student.name} {student.fathername}\n")
                elif command2 in ["cc", "cathedracourse"]:
                    sorted_list = models.Student.get_students_cathedra_course(input("Введіть кафедру: "),
                                                                              input("Введіть курс: "), students)
                    if sorted_list is None:
                        print("Немає студентів на цій кафедрі")
                        continue
                    for student in sorted_list:
                        print(f"{student.surname} {student.name} {student.fathername}\n")
                else:
                    print("Invalid command")
        elif main_menu.name == "Teachers":
            if command in ["s", "showinfo"]:
                teacher = teachers.list_of_instance[main_menu.index]
                models.Teacher.show_info(teacher, teachers)
            elif command in ["del", "delete"]:
                teacher = teachers.list_of_instance[main_menu.index]
                list_of_teacher_names.remove(f"{teacher.surname} {teacher.name} {teacher.fathername}")
                models.Teacher.delete_person(teacher, teachers)
            elif command in ["a", "add"]:
                name = input("Введіть ім'я: ")
                surname = input("Введіть прізвище: ")
                fathername = input("Введіть по-батькові: ")
                faculty = input("Введіть факультет: ")
                cathedra = input("Введіть кафедру: ")
                teacher = models.Teacher(name, surname, fathername, faculty, cathedra,)
                models.Teacher.add_person(teacher, teachers)
                list_of_teacher_names.append(f"{teacher.surname} {teacher.name} {teacher.fathername}")
            elif command in ["edit"]:
                teacher = teachers.list_of_instance[main_menu.index]
                models.Teacher.edit_person(teacher)
                list_of_teacher_names[main_menu.index] = f"{teacher.surname} {teacher.name} {teacher.fathername}"
            elif command in ["f", "find"]:
                command2 = input(
                    "Введіть за чим хочете шукати: [n]ame, "
                    "[f]athername, [s]urname, [fa]culty, [c]athedra, [p]ib >>>").strip().lower()
                if command2 in ["n", "name"]:
                    list_of_names = models.Teacher.find_list_by_name(input("Введіть ім'я: "), teachers)
                    if list_of_names is None:
                        continue
                    else:
                        for name in list_of_names:
                            print(f"Викладачі з цим ім'ям: {name.surname} {name.name} {name.fathername}")
                            models.Teacher.show_info(name, teachers)
                elif command2 in ["f", "fathername"]:
                    list_of_fathernames = models.Teacher.find_list_by_fathername(input("Введіть по-батькові: "),
                                                                                 teachers)
                    if list_of_fathernames is None:
                        continue
                    else:
                        for fathername in list_of_fathernames:
                            print(f"Викладачі з цим по-батькові:"
                                  f" {fathername.surname} {fathername.name} {fathername.fathername}")
                            models.Teacher.show_info(fathername, teachers)
                elif command2 in ["s", "surname"]:
                    list_of_surnames = models.Teacher.find_list_by_surname(input("Введіть прізвище: "), teachers)
                    if list_of_surnames is None:
                        continue
                    else:
                        for surname in list_of_surnames:
                            print(f"Викладачі з цим прізвищем: {surname.surname} {surname.name} {surname.fathername}")
                            models.Teacher.show_info(surname, teachers)
                elif command2 in ["fa", "faculty"]:
                    list_of_faculties = models.Teacher.find_list_by_faculty(input("Введіть факультет: "), teachers)
                    if list_of_faculties is None:
                        continue
                    else:
                        for faculty in list_of_faculties:
                            print(f"Викладачі цього факультету: {faculty.surname} {faculty.name} {faculty.fathername}")
                            models.Teacher.show_info(faculty, teachers)
                elif command2 in ["c", "cathedra"]:
                    list_of_cathedra = models.Teacher.find_list_by_cathedra(input("Введіть кафедру: "), teachers)
                    if list_of_cathedra is None:
                        continue
                    else:
                        for cathedra in list_of_cathedra:
                            print(f"Викладачі на цій кафедрі: {cathedra.surname} {cathedra.name} {cathedra.fathername}")
                            models.Teacher.show_info(cathedra, teachers)
                elif command2 in ["p", "pib"]:
                    list_of_pib = models.Teacher.find_list_by_pib(input("Enter name: "), input("Enter surname: "),
                                                                  input("Enter fathername: "), teachers)
                    if list_of_pib is None:
                        continue
                    else:
                        for pib in list_of_pib:
                            print(f"Викладачі з цим ПІБ: {pib.surname}{pib.name}{pib.fathername}")
                            models.Teacher.show_info(pib, teachers)
                else:
                    print("Invalid command")
            elif command in ["g", "get"]:
                command2 = input(
                    "Введіть за чим хочете шукати: [a]lphabet, "
                    "alphabet on [f]aculty, [c]ourse, [cc]thedra [course >>>").strip().lower()
                if command2 in ["a", "alphabet"]:
                    sorted_list = models.Teacher.get_by_alphabet(teachers)
                    for teacher in sorted_list:
                        print(f"{teacher.surname} {teacher.name} {teacher.fathername}\n")
                elif command2 in ["f", "faculty"]:
                    sorted_list = models.Teacher.get_by_alphabet_on_faculty(input("Введіть факультет: "), teachers)
                    if sorted_list is None:
                        print("Немає вчителів на цьому факультеті")
                        continue
                    for teacher in sorted_list:
                        print(f"{teacher.surname} {teacher.name} {teacher.fathername}\n")
                    if sorted_list is None:
                        print("Немає вчителів на цій кафедрі")
                        continue
                    for teacher in sorted_list:
                        print(f"{teacher.surname} {teacher.name} {teacher.fathername}\n")
                else:
                    print("Invalid command")
        elif main_menu.name == "Faculties":
            if command in ["a", "add"]:
                name = input("Введіть назву факультету:")
                field_of_study = input("Введіть область вивчення: ")
                faculty = models.Faculty(name, field_of_study)
                models.Faculty.add_instance(faculty, faculties)
                list_of_faculty_names.append(f"{faculty.name}")
                print(f"Факультет '{faculty.name}' додано.")
            elif command in ["e", "edit"]:
                faculty = faculties.list_of_instance[main_menu.index]
                models.Faculty.edit_system_instance(faculty)
            elif command in ["del", "delete"]:
                faculty = faculties.list_of_instance[main_menu.index]
                models.Faculty.delete_instance(faculty, faculties)
                list_of_faculty_names.remove(faculty.name)
        elif main_menu.name == "Cathedras":
            if command in ["a", "add"]:
                name = input("Введіть назву кафедри:")
                field_of_study = input("Введіть область вивчення: ")
                cathedra = models.Cathedra(name, field_of_study)
                models.Cathedra.add_instance(cathedra, cathedras)
                list_of_cathedra_names.append(f"{cathedra.name}")
                print(f"Кафедру '{cathedra.name}' додано.")
            elif command in ["e", "edit"]:
                cathedra = cathedras.list_of_instance[main_menu.index]
                models.Cathedra.edit_system_instance(cathedra)
            elif command in ["del", "delete"]:
                cathedra = cathedras.list_of_instance[main_menu.index]
                models.Cathedra.delete_instance(cathedra, cathedras)
                list_of_cathedra_names.remove(cathedra.name)
            else:
                print("Invalid command")
        else:
            print("Invalid command")
    except errors.ItemNotFoundError:
        continue
    except errors.ItemExistsError:
        continue
