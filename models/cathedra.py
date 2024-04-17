from system import System


class Cathedra(System):
    def __init__(self, name=None, field_of_study=None):
        super().__init__(name, field_of_study)
        self.dict_of_cathedra = {}

    def add_instance_to_dict(self):
        System.dict_of_system[self.__class__.__name__] = self.dict_of_cathedra
