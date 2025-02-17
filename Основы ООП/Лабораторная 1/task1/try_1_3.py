from typing import Union


class Car:
    def __init__(self, speed: Union[int, float]):
        self.speed = None  # Устанавливаем атрибут, но значение задаём позже
        self.init_speed(speed)

    def init_speed(self, speed: Union[int, float]) -> None:
        """
        Инициализирует скорость машины.

        :param speed: Начальная скорость машины.
        :type speed: Int, float
        :raises TypeError: Если скорость не является числом.
        :raises ValueError: Если скорость отрицательная.
        :return: None
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость должна быть числом.")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной.")
        self.speed = speed

    def increase_speed(self, var: Union[int, float]) -> None:
        """
        Увеличивает скорость машины.

        :param var: Скорость, прибавляемая к существующей скорости.
        :type var: Int, float
        :raises TypeError: Если скорость не является числом.
        :raises ValueError: Если скорость отрицательная.
        :return: None
        """
        if not isinstance(var, (int, float)):
            raise TypeError("Скорость должна быть числом.")
        if var < 0:
            raise ValueError("Введите положительное число")
        self.speed += var

if __name__ == "__main__":
    car = Car(20)
    car.increase_speed(10)
    print(car.speed)
