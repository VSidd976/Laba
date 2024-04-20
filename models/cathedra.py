from system import *


class Cathedra(System):

    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)


math_cathedra = Cathedra("Math", "All that connected to math")
economy_cathedra = Cathedra("Economy", "All that connected to economy")
NaUKMA.add_instance_to_dict(math_cathedra, cathedras)
NaUKMA.add_instance_to_dict(economy_cathedra, cathedras)


if __name__ == "__main__":
    print(cathedras.dict_of_instance)
