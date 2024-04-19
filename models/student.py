from person import Person


class Student(Person):
    def __init__(self, name, surname, fathername, faculty, specialty, course, group):
        super().__init__(name, surname, fathername, faculty)
        self.specialty = specialty
        self.course = course
        self.group = group
        self.student_dict = {}
