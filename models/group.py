from specialty import Specialty


class Group(Specialty):

    def __init__(self, name):
        super().__init__(name, field_of_study=None, id_number=None)
