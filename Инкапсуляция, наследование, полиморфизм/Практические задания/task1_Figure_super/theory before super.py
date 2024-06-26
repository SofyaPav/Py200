pass
'''
Наследование - это главный механизм для повторного использования кода.
Если нам не нужно изменять поведение метода в дочернем классе,
то можно воспользоваться реализацией родителя'''

'''
class PaperBook:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f'Книга "{self.name}"'


class EBook(PaperBook):  # наследуемся от PaperBook
    ...


ebook = EBook("Букварь")
print(ebook)  # Книга "Букварь"
'''
