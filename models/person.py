class Person:
    dict_of_people = {}

    def __init__(self, name, surname, fathername, faculty):
        self.name = name
        self.surname = surname
        self.fathername = fathername
        self.faculty = faculty

    def add_person(self):
        pass

    @classmethod
    def get_information(cls, name, surname, fathername):
        print(f"Name: {cls.name}"
              f"\nSurname: {cls.surname}"
              f"\nFathername: {cls.fathername}"
              f"\nFaculty: {cls.faculty}"
              )
