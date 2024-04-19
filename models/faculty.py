from system import System


class Faculty(System):
    dict_of_faculties = {}

    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)

    def add_instance_to_system(self):
        dict_of_faculties[self.name] = self
        System.dict_of_system["Faculty"] = Faculty.dict_of_faculties
    # Adds instance to the faculties dictionary