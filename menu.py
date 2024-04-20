
class Menu:
    def __init__(self, name: str, content: list):
        self.name = name
        self.content = content
        self.index = 0

    def display(self):
        result = f"\n{self.name}\n"
        result += "=" * 30 + "\n"
        for index, item in enumerate(self.content):
            if self.index == index:
                result += f"--> {item}\n"
            else:
                result += f"   {item}\n"
        return result

    def up(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.content) - 1

    def down(self):
        self.index += 1
        if self.index == len(self.content):
            self.index = 0


menu1 = Menu("Mohyla", ["People", "Structures"])
menu2 = Menu("People", ["Students", "Lecturers"])
menu3 = Menu("Structures", ["Cathedras", "Faculties"])
menu4 = Menu("Cathedras", ["Math", "Economics", "Biology"])
menu5 = Menu("Faculties", ["Fi", "Fen", "Fprn"])
menu6 = Menu("Students", ["Dima", "Valentin"])
menu7 = Menu("Lecturers", ["Kozir", "Mitnyk"])
menu_dict = {"Mohyla": menu1, "People": menu2,
             "Structures": menu3, "Cathedras": menu4,
             "Faculties": menu5, "Students": menu6,
             "Lecturers": menu7}
main_menu = menu1
while True:
    print(main_menu.display())
    command = input("Enter command: Up Down Open Exit ")
    if command.lower() == "u":
        main_menu.up()
    elif command.lower() == "d":
        main_menu.down()
    elif command.lower() == "o":
        main_menu = menu_dict[main_menu.content[main_menu.index]]
    else:
        break
