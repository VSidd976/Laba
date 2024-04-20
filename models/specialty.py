from faculty import Faculty


class Specialty(Faculty):
    def __init__(self, name, field_of_study, id_number=int):
        super().__init__(name, field_of_study)
        self.id_number = id_number
