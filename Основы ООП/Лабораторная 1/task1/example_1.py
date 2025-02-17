class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def remove_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)


if __name__ == "__main__":
    # Создаём покупателя
    customer = Customer("Анна", "anna@example.com")

    # Добавляем товары в корзину
    customer.add_to_cart("Ноутбук")
    customer.add_to_cart("Мышь")

    # Выводим содержимое корзины
    print(customer.cart)  # Ожидаем: ['Ноутбук', 'Мышь']

    # Удаляем товар из корзины
    customer.remove_from_cart("Мышь")

    # Проверяем, что мышь удалена
    print(customer.cart)  # Ожидаем: ['Ноутбук']
