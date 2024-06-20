from typing import Optional
import pprint
import json
import csv


class Book:

    def __init__(self, title: str, author: str, year: int, ):
        if not isinstance(title, str):
            raise TypeError(f'Переменная title должна быть типа str, а ввели тип {type(title)}')
        self.title = title

        if not isinstance(author, str):
            raise TypeError(f'Переменная author должна быть типа str, а ввели тип {type(author)}')
        self.author = author

        if not isinstance(year, int):
            raise TypeError(f'Переменная year должна быть типа int, а ввели тип {type(year)}')
        self.year = year

    def __str__(self):
        return f"Книга: '{self.title}'; Автор: '{self.author}'; Год: {self.year}"


if __name__ == '__main__':
    book = Book('Сказки', 'А.С. Пушкин', 1800)
    print(book)  # Книга: 'Сказки'; Автор: 'А.С. Пушкин'; Год: 1800

