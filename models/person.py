class Person:
    dict_of_people = {}

    def __init__(self, name, surname, fathername, faculty):
        self.name = name
        self.surname = surname
        self.fathername = fathername
        self.faculty = faculty

    def add_person(self):
        pass

    def get_information(self, name, surname, fathername):
        print(f"Name: {self.name}"
              f"\nSurname: {self.surname}"
              f"\nFathername: {self.fathername}"
              f"\nFaculty: {self.faculty}"
              )
