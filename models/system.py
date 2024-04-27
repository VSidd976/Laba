from models.naukma import NaUKMA


class System(NaUKMA):
    def __init__(self, name, field_of_study=None):
        super().__init__(name)
        self.field_of_study = field_of_study

    def edit_system_instance(self):
        new_field = input("Впишіть нову сферу "
                          "вивчення(якщо хочете залишити минулу,"
                          " впишіть '-'):")
        if new_field == '-':
            pass
        else:
            self.field_of_study = new_field
