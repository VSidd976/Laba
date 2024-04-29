from models.naukma import NaUKMA


class System(NaUKMA):
    def __init__(self, name, field_of_study=None):
        super().__init__(name)
        self.field_of_study = field_of_study

    def add_instance(self, instance_list):
        pass

    def delete_instance(self, instance_list):
        pass

    def edit_system_instance(self):
        pass
