class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"У ресторана {self.restaurant_name} есть {self.cuisine_type} ")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Вкусы мороженого:")
        for flavor in self.flavors:
            print(flavor)


my_ice_cream_stand = IceCreamStand("Лилипут", "мороженое", ["Ваниль", "Клубника", "Шоколад"])
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()
