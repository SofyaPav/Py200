

def check(a: [int, float]):
    if isinstance(a, int):
        print('это тип int')
    if isinstance(a, float):
        print('это тип float')


check(5)  # 'это тип int
