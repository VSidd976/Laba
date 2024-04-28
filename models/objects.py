import models


system = models.NaUKMA("System")
people = models.NaUKMA("People")
students = models.Person("Students")
teachers = models.Person("Teachers")
faculties = models.System("Faculties")
cathedras = models.System("Cathedras")
