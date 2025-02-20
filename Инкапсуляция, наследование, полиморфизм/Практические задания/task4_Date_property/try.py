class Class_1:
    def __init__(self, a):
        self.attr_1 = None  # Инициализируем атрибут со значением None
        self.meth_1(a)  # Вызываем метод для присвоения значения

    def meth_1(self, arg_1):
        """Метод для установки значения атрибута attr_1."""
        self.attr_1 = arg_1


if __name__ == "__main__":
    obj = Class_1(10)  # Создаем объект с атрибутом attr_1 = 10
    print(obj.attr_1)  # Вывод: 10