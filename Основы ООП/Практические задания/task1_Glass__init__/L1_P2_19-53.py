class Book:
    def __init__(self, author, pages):
        self.author = author
        self.pages = pages

    def set_pages(self, new_pages):
        if new_pages < 0:
            raise ValueError('Значение должно быть больше 0')
        self.pages = new_pages


book = Book('Гоголь', 500)
book.set_pages(-1)  # ValueError: Значение должно быть больше 0
