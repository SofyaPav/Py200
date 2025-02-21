class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value_paper):
        if not isinstance(value_paper, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value_paper <= 0:
            raise ValueError("Количество страниц должно быть больше 0")
        self._pages = value_paper


    def __str__(self):
        return f"Бумажная книга {self._name}. Автор {self._author}. Количество страниц {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value_duration):
        if not isinstance(value_duration, float):
            raise TypeError("Продолжительность должна быть числом с плавающей запятой")
        if value_duration <= 0:
            raise ValueError("Продолжительность должна быть больше 0")
        self._duration = value_duration

    def __str__(self):
        return f"Аудиокнига {self._name}. Автор {self._author}. Продолжительность {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

