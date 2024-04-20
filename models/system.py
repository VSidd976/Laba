from naukma import *


class System(NaUKMA):
    def __init__(self, name, field_of_study=None):
        super().__init__(name)
        self.field_of_study = field_of_study


cathedras = System("Cathedras")
faculties = System("Faculties")
NaUKMA.add_instance_to_dict(cathedras, system)
NaUKMA.add_instance_to_dict(faculties, system)


if __name__ == "__main__":
    print(system.dict_of_instance)
