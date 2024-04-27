import models
from menu import Menu
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
menu1 = Menu("NaUKMA", list(models.NaUKMA.dict_of_naukma.keys()))
menu2 = Menu("People", list(people.dict_of_instance.keys()))
menu3 = Menu("System", list(system.dict_of_instance.keys()))
menu4 = Menu("Cathedras", list(cathedras.dict_of_instance.keys()))
menu5 = Menu("Faculties", list(faculties.dict_of_instance.keys()))
menu6 = Menu("Students", list(students.dict_of_instance.keys()))
menu7 = Menu("Teachers", list(teachers.dict_of_instance.keys()))
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
        command = input("Enter command: Up Down GetInfo Back Exit ")
    else:
        command = input("Enter command: Up Down Open Back Exit ")
    if command.lower() == "u" or command.lower() == "up":
        main_menu.up()
    elif command.lower() == "d" or command.lower() == "down":
        main_menu.down()
    elif command.lower() == "o" or command.lower() == "open":
        main_menu = menu_dict[main_menu.content[main_menu.index]]
    elif command.lower() == "b" or command.lower() == "back":
        main_menu = menu_dict2[main_menu.name]
    elif command.lower() == "e" or command.lower() == "exit":
        break
    else:
        print("Invalid command")
