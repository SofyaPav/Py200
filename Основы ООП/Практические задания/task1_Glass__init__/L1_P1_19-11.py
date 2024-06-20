pass

'''

class A:
    def __init__(self, var1, var2):
        self.var10 = var1
        self.var20 = var2


a = A(10, 20)

print(a.var10)
'''


class B:
    def __init__(self, incoming_data_1, incoming_data_2):
        self.attribute_1 = incoming_data_1  # здесь self.attribute_1 - атрибут
        self.attribute_2 = incoming_data_2  # здесь self.attribute_2 - атрибут


b = B(7, 101)

print(b.attribute_1)
print(b.attribute_2)
