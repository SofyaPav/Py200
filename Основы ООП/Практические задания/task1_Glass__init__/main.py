from typing import Union  # Аннотация типов в функции
кеку
class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = 300
        self.occupied_volume = 100


if __name__ == "__main__":
    ...  # TODO инициализировать два объекта типа Glass

    # TODO попробовать инициализировать не корректные объекты
