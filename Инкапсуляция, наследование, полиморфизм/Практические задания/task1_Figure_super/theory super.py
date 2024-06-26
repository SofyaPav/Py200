pass
'''
Вызов конструктора родительского класса. Функция super
А если в дочернем классе, после переопределения метода __init__
все равно необходимо вызвать конструктор базового класса?

В таком случае необходимо воспользоваться встроенной функцией super().

super() эквивалентно переменной cls, только на родительский класс.
'''


'''
class BaseClass:
    def __init__(self):
        print(f'Вызван конструктор базового класса')


class SubClass(BaseClass):
    def __init__(self):
        print(f'Вызван конструктор дочернего класса')


b = BaseClass()  # Вызван конструктор базового класса
s = SubClass()  # Вызван конструктор дочернего класса
'''


class BaseClass:
    def __init__(self):
        print(f'Вызван конструктор базового класса')


class SubClass(BaseClass):
    def __init__(self):
        super().__init__()  # вызывает метод родительского класса
        print(f'Вызван конструктор дочернего класса')


b = BaseClass()
s = SubClass()


'''
Дополнение конструктора родительского класса
'''

'''
class PaperBook:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Книга "{self.name}"'


class EBook(PaperBook):
    def __init__(self, name: str):
        self.format = "pdf"


print(PaperBook("Букварь"))  # Книга "Букварь"
'''


class PaperBook:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Книга "{self.name}"'


class EBook(PaperBook):
    def __init__(self, name: str):
        super().__init__(name)  # вызываем конструктор базового класса
        self.format = "pdf"


print(EBook("Букварь"))
