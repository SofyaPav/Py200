import doctest

class Table:
    def __init__(self, height, material):
        """
        Создание и подготовка к работе объекта "Стол"

        :param height: Высота стола (в метрах)
        :param material: Материал стола

        Примеры:
        >>> table = Table(0.8, "Дерево") # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота стола должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота стола должна быть положительным числом")
        self.height = height

        if not isinstance(material, str):
            raise TypeError("Материал стола должен быть str")
        self.material = material

    def increase_height(self, value) -> None:
        """
        Увеличение высоты стола.
        :param value: Высота, прибавляемая к высоте (в метрах)

        :raise ValueError: Если высота стола превышает высоту в каталоге мебельной фабрики, то вызываем ошибку

        Примеры:
        >>> table = Table(0.8, "Дерево")
        >>> table.increase_height(0.1)
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if value <= 0:
            raise ValueError("Высота должна быть положительным числом")
        ...

    def change_material(self, new_material) -> None:
        """
        Изменение материала стола.
        :param new_material: Новый материал стола

        :raise ValueError: Если новый материал стола отсутствует в каталоге мебельной фабрики, то вызываем ошибку

        Примеры:
        >>> table = Table(0.8, "Дерево")
        >>> table.change_material("Сталь")
        """
        if not isinstance(new_material, str):
            raise TypeError("Материал стола должен быть str")
        ...


class Car:
    def __init__(self, color, speed):
        """
        Создание и подготовка к работе объекта "Машина"

        :param color: Цвет машины
        :param speed: Скорость машины

        Примеры:
        >>> car = Car("Красный", 100) # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет машины должен быть str")
        self.color = color

        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость машины должна быть типа int или float")
        if speed <= 0:
            raise ValueError("Скорость машины должна быть положительным числом")
        self.speed = speed

    def change_color(self, new_color) -> None:
        """
        Изменение цвета машины.
        :param new_color: Новый цвет машины

        :raise ValueError: Если новый цвет машины не предоставляется в автосервисе

        Примеры:
        >>> car = Car("Красный", 100)
        >>> car.change_color("Жёлтый")
        """
        if not isinstance(new_color, str):
            raise TypeError("Цвет машины должен быть str")
        ...


    def decrease_speed(self, new_speed) -> None:
        """
        Уменьшение скорости машины.
        :param new_speed: Скорость, отнимаемая от текущей скорости (км/ч)

        :raise ValueError: Если величина отнимаемой скорости превышает текущую скорость, то вызываем ошибку

        Примеры:
        >>> car = Car("Красный", 100)
        >>> car.decrease_speed(10)
        """
        if not isinstance(new_speed, (int, float)):
            raise TypeError("Скорость машины должна быть типа int или float")
        if new_speed <= 0:
            raise ValueError("Скорость машины должна быть положительным числом")


class SocialNetwork:
    def __init__(self, name, number_of_users):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Имя социальной сети
        :param number_of_users: Количество зарегистрированных пользователей

        Примеры:
        >>> social_network= SocialNetwork("VK", 2000000) # инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Имя социальной сети должно быть str")
        self.name = name

        if not isinstance(number_of_users, int):
            raise TypeError("Количество зарегистрированных пользователей должно быть типа int")
        if number_of_users <= 0:
            raise ValueError("Количество зарегистрированных пользователей должно быть положительным числом")
        self.number_of_users = number_of_users

    def change_name(self, new_name) -> None:
        """
        Изменение имени социальной сети.
        :param new_name: Новое имя социальной сети

        :raise ValueError: Если новое имя совпадает с именем уже существующей популярной социальной сети

        Примеры:
        >>> social_network= SocialNetwork("VK", 2000000)
        >>> social_network.change_name("Vkontakte")
        """
        if not isinstance(new_name, str):
            raise TypeError("Имя социальной сети должно быть str")
        ...


    def add_users(self, new_users) -> None:
        """
        Увеличение количества зарегестрированныз пользователей.
        :param new_users: Количество новых пользователей

        :raise ValueError: Если сумма новых и существующих пользователей превышает населения Земли

        Примеры:
        >>> social_network= SocialNetwork("VK", 2000000)
        >>> social_network.change_name("Vkontakte")
        """
        if not isinstance(new_users, int):
            raise TypeError("Количество новых зарегистрированных пользователей должно быть типа int")
        if new_users <= 0:
            raise ValueError("Количество новых зарегистрированных пользователей должно быть положительным числом")
        ...

if __name__ == "__main__":
    doctest.testmod()