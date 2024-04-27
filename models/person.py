from naukma import NaUKMA


class Person(NaUKMA):
    def __init__(self, name, surname=None, fathername=None, faculty=None):
        super().__init__(name)
        self.surname = surname
        self.fathername = fathername
        self.faculty = faculty

    def add_person(self, person):
        pass

    def delete_person(self, person):
        pass

    def show_info(self):
        pass

    def edit_person(self):
        pass
