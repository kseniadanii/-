class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Название {self.restaurant_name} ')
        print(f'Тип кухни {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} открыт')


restaurant1 = Restaurant('Итальяно', 'Итальянская кухня')
restaurant2 = Restaurant('Францужи', 'Французская кухня')
restaurant3 = Restaurant('Мексикано', 'Мексиканская кухня')

restaurant1.describe_restaurant()

restaurant2.describe_restaurant()

restaurant3.describe_restaurant()
