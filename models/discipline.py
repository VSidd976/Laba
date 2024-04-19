# потім треба замінити всі імпорти на імпорт ініт

from cathedra import Cathedra


class Discipline(Cathedra):
    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)

    def add_instance_to_system(self):
        pass
