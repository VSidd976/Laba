from system import System


class Faculty(System):
    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)
        self.faculties = {}

    def add_instance_to_dict(self):
        System.dict_of_system[self.__class__.__name__] = self.faculties
