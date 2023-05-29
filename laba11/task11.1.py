class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Название {self.restaurant_name} ')
        print(f'Тип кухни {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} открыт')


#restaurant = Restaurant('Лилипут', 'Детская')
newRestaurant = Restaurant('Котиколенд', 'Кошачья')
#print(restaurant.restaurant_name)
#print(restaurant.cuisine_type)
#restaurant.describe_restaurant()
#restaurant.open_restaurant()
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
