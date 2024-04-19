class Menu:
    def __init__(self, name, content):
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

    def use(self, name, content):
        new_menu = Menu(name, content)
        return new_menu.display()
#dick = {"Mohyla": ["People", "Structures", "Exit"]
 #       "People": ["Students","Lecturers"]
  #      "Structures": ["Cathedra", "Faculties"]}



name = "Mohyla"
content = ["People", "Structures", "Exit"]
menu = Menu(name, content)
print(menu.display())
menu.up()
print(menu.display())
menu.up()
print(menu.display())
menu.down()
print(menu.display())
menu.down()
print(menu.display())
menu2 = Menu("People", ["Students", "Lecturers"])
menu3 = Menu("Structures", ["Cathedra", "Faculties"])
print(menu2.display())
print(menu3.display())
print(menu.use("People", ["Students"]))

