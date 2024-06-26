import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
        def __init__(self):
            super().__init__()

            self.length = length

        def area(self):
            return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Figure):
    """ Производный класс. Круг. """

    ...  # TODO определить конструктор и перегрузить метод area


if __name__ == "__main__":
    fig = Figure()
    fig.area()

    rect = Rectangle(5, 10)
    rect.area()

    circle = Circle(5)
    circle.area()
