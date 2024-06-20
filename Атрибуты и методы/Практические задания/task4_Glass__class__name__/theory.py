pass

'''
https://colab.research.google.com/drive/1eQ-8lG0b-eunGyUmM_XLKYsRA9_V0CO3?usp=sharing#scrollTo=q5cm4wvcg34Q
Магический метод __repr__ определяет поведение функции repr(),
вызванной для экземпляра вашего класса.

Метод должен возвращать строку, показывающую,
как может быть инициализирован экземпляр.
'''


class Book:
    def __init__(self, name: str):
        self.name = name


book = Book("Букварь")
print(repr(book))  # <__main__.Book object at 0x00000257A48B4FD0>
print(f"{book}")  # <__main__.Book object at 0x00000257A48B4FD0>
print(f"{book!r}")  # <__main__.Book object at 0x00000257A48B4FD0>

'''Что делает !r '''

a = 'Строчка'
print(a)  # Строчка
print(f'{a!r}')  # 'Строчка'


'''
https://sky.pro/media/raznicza-mezhdu-__str__-i-__repr__-v-python/
Часто при работе с объектами в Python возникает потребность в представлении объектов в виде строк. 
Это может быть полезно для отладки, логирования или просто для вывода информации о объекте. 
В Python для этого существуют два специальных метода: __str__ и __repr__. 
Предположим, что есть класс Cat, который имеет атрибуты name и age. 
Можно было бы представить объект этого класса в виде строки следующим образом:
'''


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Cat(name={self.name}, age={self.age})'


animal_1 = Cat('Маруся', 1)
print(animal_1)  # Cat(name=Маруся, age=1)
print(str(animal_1))  # Cat(name=Маруся, age=1)

'''
Однако, что если нужно получить более детальное или иное представление объекта, 
которое будет удобно использовать для отладки или логирования? 
Здесь на помощь приходит метод __repr__.

Метод __repr__ предназначен для создания «официального» строкового представления объекта, 
которое может быть использовано для воссоздания объекта при помощи функции eval(). 
Вернувшись к нашему примеру с классом Cat, можно добавить метод __repr__ следующим образом:
'''


class Kitty:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Kitty(name={self.name}, age={self.age})'

    def __repr__(self):
        return f'Kitty(name={self.name!r}, age={self.age!r})'


animal_2 = Kitty('Сима', 0.5)
print(str(animal_2))  # Kitty(name=Сима, age=0.5)
print(repr(animal_2))  # Kitty(name='Сима', age=0.5) - появились кавычки "Сима"

'''
Важно отметить, что если для класса определен только метод __repr__, 
то он будет использован и при вызове str(). 
Однако, если определены оба метода, __str__ и __repr__, 
то при вызове str() будет использован __str__, а при вызове repr() — __repr__.
'''