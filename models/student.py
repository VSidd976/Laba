from person import Person


class Student(Person):
    def __init__(self, name, surname, fathername, faculty, specialty, course, group=None):
        super().__init__(name, surname, fathername, faculty)
        self.specialty = specialty
        self.course = course
        self.group = group
        # Тут group за замовчуванням None, бо не на всіх спеціальностях є групи
        # Якщо в студента за пеціальністю є група, то її можна просто вказати, але при тому в студента
        # в якого немає групи не буде проблем з тим, що йому треба заповнювати це поле
