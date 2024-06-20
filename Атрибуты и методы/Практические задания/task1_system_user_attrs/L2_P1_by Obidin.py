from typing import Optional
import pprint
import json
import csv


class Book:
    id_book = 0

    def __init__(self, title: str, author: str, year: int, book_id: [int, None] = None):
        if not isinstance(title, str):
            raise TypeError(f'Переменная title должна быть типа str, а ввели тип {type(title)}')
        self.title = title

        if not isinstance(author, str):
            raise TypeError(f'Переменная author должна быть типа str, а ввели тип {type(author)}')
        self.author = author

        if not isinstance(year, int):
            raise TypeError(f'Переменная year должна быть типа int, а ввели тип {type(year)}')
        self.year = year

        if not isinstance(book_id, (int, type(None))):
            raise TypeError(f'Переменная book_id должна быть типа int, а ввели тип {type(book_id)}')
        if book_id is None:
            self.book_id = self.get_id_book()
        else:
            self.book_id = book_id

    @classmethod
    def get_id_book(cls):
        cls.id_book += 1
        return cls.id_book

    def __str__(self):
        return f"ID: {self.book_id}; Книга: '{self.title}'; Автор: '{self.author}'; Год: {self.year}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, year={self.year!r}, book_id={self.book_id!r})"


class Library:
    def __init__(self, books: Optional[list[Book]] = None):
        if books is None:
            self.books = []
        elif not isinstance(books, list):
            raise TypeError(f'Переменная books должна быть типа list, а ввели тип {type(books)}')
        else:
            self.books = books

    def __str__(self):
        return self.view_str_table(self.books)

    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError(f'Переменная book должна быть типа Book, а ввели тип {type(book)}')
        self.books.append(book)
        print(f'Добавлена книга {book}')

    def delete_book(self, id_book):
        for book in self.books:
            if book.book_id == id_book:
                self.books.remove(book)
                print(f"Удалена книга {book}")
                return
        print(f"Книга с id = {id_book} не найдена")

    @staticmethod
    def view_str_table(list_books):
        table = ''
        header = f"| {'ID':4}| {'Название':30}| {'Автор':20}| {'Год':4}|"
        close_header = '-'*len(header)

        table += close_header + '\n'
        table += header + '\n'
        table += close_header + '\n'
        if list_books:
            for book in list_books:
                table += f"| {book.book_id!r:4}| {book.title!r:30}| {book.author!r:20}| {book.year!r:4}|" + '\n'
        else:
            table += "Библиотека пустая" + '\n'
        table += close_header + '\n'

        return table

    def view_books(self, list_books: [list[Book], None] = None):
        if list_books is None:
            print(self.view_str_table(self.books))
        else:
            print(self.view_str_table(list_books))

    def find_books(self, title=None, author=None):
        found_books = []

        if title:
            found_books.extend([book for book in self.books if title.lower() in book.title.lower()])

        if author:
            found_books.extend([book for book in self.books if author.lower() in book.author.lower() and book not in found_books])

        self.view_books(found_books)

    def clear(self):
        self.books.clear()
        print('Библиотека успешно очищена')


if __name__ == '__main__':
    book = Book('Сказки', 'А.С. Пушкин', 1800, 1)
    # a = [1,2,3,4,5,6]
    # print(a)
    # print(book)
    lib = [Book('Сказки', 'А.С. Пушкин', 1800, 1),
           Book('Сказки', 'А.С. Пушкин', 1800, 2),
           Book('Сказки', 'А.С. Пушкин', 1800, 3)]

    # print(lib)

    library = Library(books=lib)
    pprint.pprint(library.books)

    library.view_books()

    print(Library())
    print(library)

    library.add_book(Book('Сказки', 'А.С. Пушкин', 1800, 1))

    print(library)

    library.delete_book(1)
    library.delete_book(1)
    print(library)
    library.delete_book(1)

    with open('books.json', encoding='utf-8') as file:
        data = json.load(file)

    # with open('books.csv', encoding='utf-8') as file:
    #     reader = csv.DictReader(file, delimiter=';')
    #     data = [book for book in reader]

    for book in data:
        # library.add_book(Book(title=book['title'],
        #                       author=book['author'],
        #                       year=book['year'],
        #                       book_id=book['book_id']))
        library.add_book(Book(**book))

    print(library)

    list_books = [Book(**data_book) for data_book in data]

    library1 = Library(books=list_books)

    print(library1)

    library2 = Library()
    print(library2)

    library2.add_book(Book('Сказки', 'А.С. Пушкин', 1800))
    library2.add_book(Book('Сказки', 'А.С. Пушкин', 1800))
    library2.add_book(Book('Сказки', 'А.С. Пушкин', 1800))
    library2.add_book(Book('Сказки', 'А.С. Пушкин', 1800))
    library2.add_book(Book('Сказки', 'А.С. Пушкин', 1800))
    library2.add_book(Book('Сказки', 'А.С. Пушкин', 1800))
    library2.add_book(Book('Сказки', 'А.С. Пушкин', 1800))
    library2.add_book(Book('Сказки', 'А.С. Пушкин', 1800, 10))
    library2.add_book(Book('Сказки', 'А.С. Пушкин', 1800))
    print(library2)
    library2.delete_book(6)
    library2.delete_book(2)
    print(library2)
    library2.add_book(Book('Сказки', 'А.С. Пушкин', 1800))
    library2.add_book(Book('Сказки', 'А.С. Пушкин', 1800))
    library2.add_book(Book('Сказки', 'А.С. Пушкин', 1800))
    print(library2)

    library1.find_books(author='Иван')

















