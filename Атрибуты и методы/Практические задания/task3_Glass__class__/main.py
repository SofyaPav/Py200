class Glass:
    ...


if __name__ == "__main__":  # т.к. мы запуск. из этого файла то True => автоматически запускается всё далее
    glass = Glass()

    print(type(glass))  # <class '__main__.Glass'>
    print(glass.__class__)  # <class '__main__.Glass'>

    print(type(glass) is glass.__class__)  # True
