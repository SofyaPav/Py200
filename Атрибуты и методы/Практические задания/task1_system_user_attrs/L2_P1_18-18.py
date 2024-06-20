pass

'''
not - логический оператор, который возвращает True, если утверждение не True. 
В общем возвращает противоположное значение
То есть:
not True  # False
not False  # True
'''

class Book:
    def __init__(self, title: str):
        if not isinstance(title, str):  # Если фун isinstance выдает False, то not делает его True и, цикл запускается
            raise TypeError(f'Переменная title должна быть типа str, а вы ввели тип {type(title)}')
        self.title = title


if __name__ == '__main__':
    book = Book(5)  # TypeError: Переменная title должна быть типа str, а вы ввели тип <class 'int'>
