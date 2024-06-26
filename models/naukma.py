class NaUKMA:
    dict_of_naukma = {}

    def __init__(self, name):
        self.name = name
        self.dict_of_instance = {}
        self.list_of_instance = []
        # Цей dict_of_instance буде успадковуватись у всіх дочірніх класах.
        # Тобто при створенні екземпляра дочірнього класу в нього буде автоматично створюватись свій словник
        # Так само для list_of_members, тільки він вже буде використовуватись, коли дійдемо до кінця матрьошки

    def add_instance_to_naukma(self):
        NaUKMA.dict_of_naukma[self.name] = self
    # """Цей метод чисто для того, щоб додати ключі System та People в dict_of_naukma та їхні об'єкти
    # У мене в ідеї на початку створити об'єкти System та People та пододавати їх у словник
    # Це будуть об'єкти класу NaUKMA"""

    def add_instance_to_dict(self, instance):
        instance.dict_of_instance[self.name] = self
    # Цей метод для дочірніх класів, щоб його по 100 разів не писати в дочіпніх класах
    # Просто треба буде вказати до словника якого об'єкта ми хочемо додати наступний об'єкт по матрьошці

    def add_instance_to_list(self, instance):
        instance.list_of_instance.append(self)
    # Цей метод для того, щоб додавати об'єкти дочірніх класів, які стоять у кінці матрьошки
    # Типу об'єкти класу Student або Teacher
