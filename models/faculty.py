from system import *


class Faculty(System):

    def __init__(self, name, field_of_study):
        super().__init__(name, field_of_study)


fi = Faculty('FI', "Informatics")
fen = Faculty('FEN', "Economy")
NaUKMA.add_instance_to_dict(fi, faculties)
NaUKMA.add_instance_to_dict(fen, faculties)


if __name__ == "__main__":
    print(faculties.dict_of_instance)
