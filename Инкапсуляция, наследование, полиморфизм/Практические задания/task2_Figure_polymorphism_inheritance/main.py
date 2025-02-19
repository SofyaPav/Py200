import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
        def __init__(self, length: float, width: float):
            self.length = length
            self.width = width

        def area(self) -> float:
            print(f"Вызван метод класса {self.__class__.__name__}")
            return self.length * self.width  # Формула площади прямоугольника




class Circle(Figure):
    """ Производный класс. Круг. """

    def __init__(self, radius: float):
        self.radius = radius  # TODO определить конструктор и перегрузить метод area

    def area(self) -> float:
        print(f"Вызван метод класса {self.__class__.__name__}")
        return math.pi * self.radius ** 2  # Формула площади круга

if __name__ == "__main__":
    fig = Figure()
    fig.area()

    rect = Rectangle(5, 10)
    rect.area()

    circle = Circle(5)
    circle.area()
