class Food:
    count = 0

    def __init__(self, name, food_type, price):
        self.name = name
        self.type = food_type
        self.price = price

    def __str__(self):
        return f'{self.type} "{self.name}" ({self.price})'


class Drink:
    count = 0

    def __int__(self, name, taste, amount=1):
        self.name = name
        self.taste = taste
        self.amount = amount

    def __str__(self):
        return f'{self.name} ({self.taste}) ({self.amount})'


meat = Food("Говядина", "Мясо", 200)
print(meat)

vegetables = Food('Помидоры', 'Овощи', 50)
print(vegetables)










