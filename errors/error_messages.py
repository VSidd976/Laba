class BaseError(Exception):
    ERROR_CODE = 0

    def __init__(self, message):
        self._error = self.ERROR_CODE
        self._message = message

    def __str__(self) -> str:
        return f"Error:{self._error:02d} - '{self._message}'"


class RangeError(BaseError):
    ERROR_CODE = 1

    def __init__(self, message):
        super().__init__(message)
        # self.message = "Неправильний тип. Існуючі курси: 1, 2, 3, 4, М-1, М-2"


class NoInputError(BaseError):
    ERROR_CODE = 2

    def __init__(self, message):
        super().__init__(message)
        # self.message = "Не може бути пустого поля при введенні параметру"


class ItemNotFoundError(BaseError):
    ERROR_CODE = 3

    def __init__(self, message):
        super().__init__(message)


class ItemExistsError(BaseError):
    ERROR_CODE = 4

    def __init__(self, message):
        super().__init__(message)
