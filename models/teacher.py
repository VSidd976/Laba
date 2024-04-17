from person import Person


class Teacher(Person):
    def __init__(self, name, surname, fathername, faculty, cathedra):
        super().__init__(name, surname, fathername, faculty)
        self.cathedra = cathedra
        self.teacher_dict = {}

    def add_person(self):
        Person.dict_of_people[self.__class__.__name__] = self.teacher_dict
