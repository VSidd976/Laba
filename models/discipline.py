from cathedra import *


class Discipline(Cathedra):
    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)

    def add_discipline(self, cathedra):
        # cathedra - кафедра в яку додаємо дисципліну
        if self not in cathedra.list_of_instance:
            NaUKMA.add_instance_to_list(self, cathedra)
            print(f"Дисципліну '{self.name}' додано.")
        else:
            print(f"Дисципліна '{self.name}' вже існує.")
    # Додає кафедру і її значення в словнику матрьошці

    def delete_discipline(self, cathedra):
        if self not in cathedra.list_of_instance:
            print(f"Дисципліни '{self.name}' не існує.")
        else:
            cathedra.list_of_instance.remove(self)
            print(f"Дисципліну '{self.name}' видалено.")
    # Видаляє факультет і її ключ зі значенням в словнику матьошц


dm = Discipline("Discrete Math", "All that is not in analysis")
ma = Discipline("Math Analysis", "All that analysis learns")
# NaUKMA.add_instance_to_list(dm, math_cathedra)
# NaUKMA.add_instance_to_list(ma, math_cathedra)


if __name__ == "__main__":
    dm.add_discipline(math_cathedra)
    ma.add_discipline(math_cathedra)
    dm.delete_discipline(math_cathedra)
    ma.delete_discipline(math_cathedra)
    print(math_cathedra.list_of_instance)
