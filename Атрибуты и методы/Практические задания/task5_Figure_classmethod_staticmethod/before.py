class TriangleCalculator:
    """ Класс-калькулятор площадей треугольников. """

    # TODO сделать методом класса
    def area(self, *args):
        """
        Метод, который считает площадь по разным формулам,
         в зависимости от количества переданных аргументов.
        """
        if len(args) == 2:
            self.area_by_height(*args)
        if len(args) == 3:
            self.area_by_angle(*args)

    def area_by_angle(self, a, b, angle):  # TODO сделать статическим методом
        """ Формула площади по двум сторонам и углу между ними. """
        return 0.5 * a * b * math.sin(angle)

    def area_by_height(self, a, h):  # TODO сделать статическим методом
        """ Формула площади по основанию и высоте. """
        return 0.5 * a * h


if __name__ == '__main__':
    TriangleCalculator().area()  # Работаем через экземпляр
    TriangleCalculator().area_by_height(5, 10)  # Работаем через экземпляр


