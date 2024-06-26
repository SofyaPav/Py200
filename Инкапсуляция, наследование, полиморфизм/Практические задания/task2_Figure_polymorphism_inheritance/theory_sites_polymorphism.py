from math import pi
pass

'''
https://habr.com/ru/articles/552922/
Полиморфизм и наследование
Как и в других языках программирования, в Python дочерние классы могут наследовать методы и 
атрибуты родительского класса. Мы можем переопределить некоторые методы и атрибуты специально для того, 
чтобы они соответствовали дочернему классу, и это поведение нам известно как переопределение метода(method overriding).

Полиморфизм позволяет нам иметь доступ к этим переопределённым методам и атрибутам, которые имеют то же самое имя, 
что и в родительском классе.
'''


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")  # здесь "Square" - required positional argument: 'name'

        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")  # здесь "Circle" - required positional argument: 'name'
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
'''

Здесь мы можем увидеть, что такие методы как __str__(), которые не были переопределены в дочерних классах, 
используются из родительского класса.

Благодаря полиморфизму интерпретатор питона автоматически распознаёт, что метод fact() 
для объекта a(класса Square) переопределён. И использует тот, который определён в дочернем классе.

С другой стороны, так как метод fact() для объекта b не переопределён, то используется метод с таким именем 
из родительского класса(Shape).

'''