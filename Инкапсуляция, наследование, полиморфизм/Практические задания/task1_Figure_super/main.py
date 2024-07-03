class Figure:
    def __init__(self, name=None):
        self.name = name

    def print_name(self):
        print(self.name)


class Rectangle(Figure):
    def __init__(self, a, b, *args):
        super().__init__(*args)
        self.a = a
        self.b = b


if __name__ == "__main__":
    rect = Rectangle(5, 10, 'rect_fig')
    rect.print_name()
