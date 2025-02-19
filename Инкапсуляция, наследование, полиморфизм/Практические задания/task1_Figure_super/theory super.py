class Parent:
    def say_hello(self):
        print("Привет от родителя!")

class Child(Parent):
    def introduce(self):
        super().say_hello()  # Вызываем метод родителя
        print("А теперь представляется ребенок!")

child = Child()
child.introduce()