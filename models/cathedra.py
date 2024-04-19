from system import System


class Cathedra(System):
    dict_of_cathedras = {}

    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)

    def add_instance_to_system(self):
        dict_of_cathedras[self.name] = self
        System.dict_of_system["Cathedra"] = Cathedra.dict_of_cathedras
    # Adds instance to the cathedras dictionary