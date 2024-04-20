from person import Person


class Teacher(Person):
    def __init__(self, name, surname, fathername, faculty, cathedra):
        super().__init__(name, surname, fathername, faculty)
        self.cathedra = cathedra
