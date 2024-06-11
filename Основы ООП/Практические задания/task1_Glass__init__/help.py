"""Создание экземпляра класса"""


class Book:  # создали класс по имени 'Book'
    def __init__(self):  # Метод __init__ подгот. создан. объ. к использованию
        self.author = 'Пушкин А.С.'  # атрибут - перемен., но относится к объ. опред. типа
        self.pages = 500  # атрибут тоже


# Объекты класса Book, готовые к использованию, вызываем их
book_1 = Book()
book_2 = Book()
print(book_1)
print(book_2)

book_3 = Book('Автор', 50)
print(book_3)


'''
функция type() позволяет определить тип объекта,
т.е. класс , от которого создан объект
в python всё является объектами
'''
print(type(1))  # <class 'int'>
print(type("str"))  # <class 'str'>
print(type(None))  # <class 'NoneType'>


def fun(str_):
    return str_


print(type(fun))  # <class 'function'>


class Box:  # создали класс по имени 'Box'
    def __init__(self):  # Метод __init__ подгот. создан. объ. к использованию
        self.width = 1000  # атрибут - перемен., но относится к объ. опред. типа
        self.height = 700  # атрибут тоже


box_1 = Box()  # инициализируем экземпляр класса
print(box_1)  # печатаем экземпляр класса
print(type(box_1))  # печатаем тип экземпляра класса

print(type(Box))  # печатаем тип самого класса

'''
isinstance( ) принимает объект и его предполагаемый тип, 
выдает True, если тип соответствует объекту,
выдает False, если тип не соответствует объекту

шаблон:
isinstance(object_, type_)
'''

# Проверяем является ли a = [1, 4, 8] списком
a = [1, 4, 8]
print(isinstance(a, list))  # True


