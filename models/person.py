from naukma import *
# import random


class Person(NaUKMA):
    # list_of_id = []

    def __init__(self, name, surname=None, fathername=None, faculty=None):
        super().__init__(name)
        self.surname = surname
        self.fathername = fathername
        self.faculty = faculty
    #     def get_random_id():
    #         id = int
    #         if len(Person.list_of_id) == 1000000:
    #             print("Max people achieved")
    #         #  Треба написати для цього окремий рейз помилки
    #         random_id = random.randint(1, 1000000)
    #         if random_id not in Person.list_of_id:
    #             id = random_id
    #         else:
    #             get_random_id()
    #         return id
    #     self.id = get_random_id()
    #
    # def add_instance_to_dict(self, instance):
    #     instance.dict_of_instance[self.id] = self
    # ""Я хочу оцю штуку, що у великому коменті прибрати, бо вона не потрібна, бо, коли ми доходимо до кінця
    # матрьошки, то ми працюємо вже зі списками, а не словниками. Для цього я створив метод
    # add_instance_to_list у NaUKMA"""

    def add_person(self, person):
        pass

    def delete_person(self, person):
        pass

    def edit_person(self):
        pass


students = Person("Students")
teachers = Person("Teachers")
NaUKMA.add_instance_to_dict(students, people)
NaUKMA.add_instance_to_dict(teachers, people)


if __name__ == "__main__":
    print(people.dict_of_instance)
