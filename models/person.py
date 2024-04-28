from models.naukma import NaUKMA


class Person(NaUKMA):
    def __init__(self, name, surname=None, fathername=None, faculty=None, cathedra=None):
        super().__init__(name)
        self.surname = surname
        self.fathername = fathername
        self.faculty = faculty
        self.cathedra = cathedra

    def add_person(self, person):
        pass

    def delete_person(self, person):
        pass

    def edit_person(self):
        pass
