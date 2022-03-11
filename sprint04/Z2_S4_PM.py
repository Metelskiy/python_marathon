class Pizza:
    order=0
    #hawaiian=["ham","pineapple"]
    def __init__(self, ingredients, order_number=0):
        Pizza.order+=1
        self.order_number=order_number
        self.ingredients = ingredients
        self.order_number=Pizza.order
    @classmethod
    def hawaiian(cls):
        ingredients = ["ham", "pineapple"]
        return cls(ingredients)
    @classmethod
    def meat_festival(cls):
        ingredients = ["beef", "meatball", "bacon"]
        return cls(ingredients)
    @classmethod
    def garden_feast(cls):
        ingredients = ["spinach","olives","mushroom"]
        return cls(ingredients)

p1=Pizza(["bacon", "parmesan", "ham"])
p2=Pizza.hawaiian()
p3=Pizza.meat_festival()
p4=Pizza.garden_feast()
print(p1.ingredients)
print(p2.ingredients)
print(p3.ingredients)
print(p4.ingredients)
print(p1.order_number)
print(p2.order_number)
print(p3.order_number)
print(p4.order_number)
