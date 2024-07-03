from typing import Union


class Glass:
    var = 10
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        print(self.__dict__)
        self.capacity_volume = capacity_volume  # объем стакана
        self.occupied_volume = occupied_volume  # объем жидкости в стакане
        print(self.__dict__)

    def __str__(self):
        return f"Стакан с объемом {self.capacity_volume}, заняли {self.occupied_volume}"

    def __repr__(self):
        return f"Glass({self.capacity_volume!r}, {repr(self.occupied_volume)})"


if __name__ == "__main__":
    glass = Glass(200, 100)
    a = [1,2,3,4,5]
    print(a)
    print(glass)
    print([[Glass(200, 100), Glass('200', 100), Glass(200, '100')]])
    glass.volume = 100
    print(glass.__dict__)
    glass.__dict__['volume3'] = 300
    print(glass.__dict__)
    print(glass.volume3)

