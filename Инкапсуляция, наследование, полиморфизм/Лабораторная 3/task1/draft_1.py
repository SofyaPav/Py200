


class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self.name

    @property
    def author(self):
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = None
        self.check_paper(pages)

    def check_paper(self, value_paper):
        if not isinstance(value_paper, int):
            raise TypeError
        self.pages = value_paper

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = None
        self.check_audio(duration)

    def check_audio(self, value_audio):
        if not isinstance(value_audio, float):
            raise TypeError
        self.duration = value_audio

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
