


class Glass:

    def __init__(self, capacity_volume, occupied_volume):
        self.capacity_volume = capacity_volume  # объем стакана
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

    def __repr__(self):
        # self.__class__.__name__ вместо явного указания названия класса
        return f"{self.__class__.__name__}({self.capacity_volume}, {self.occupied_volume})"


if __name__ == "__main__":
    glass = Glass(200, 100)
    print(glass)

