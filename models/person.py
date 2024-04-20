from naukma import *


class Person(NaUKMA):

    def __init__(self, name, surname=None, fathername=None, faculty=None):
        super().__init__(name)
        self.surname = surname
        self.fathername = fathername
        self.faculty = faculty
        self.list_of_members = []


students = Person("Students")
teachers = Person("Teachers")
NaUKMA.add_instance_to_dict(students, people)
NaUKMA.add_instance_to_dict(teachers, people)


if __name__ == "__main__":
    print(people.dict_of_instance)
