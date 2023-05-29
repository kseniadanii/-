class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def change_the_rating(self, new_rating):
        print(f'Изначальный рэйтинг: {self.rating}')
        self.rating = new_rating
        print(f'Новый рейтинг: {self.rating}')

    def describe_restaurant(self):
        print(f'Название {self.restaurant_name} ')
        print(f'Тип кухни {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} открыт')


new = int(input(f"Какой новый рейтинг? "))
new1 = int(input(f"Какой новый рейтинг? "))
restaurant = Restaurant('Лилипут', 'Детская', 2)
restaurant2 = Restaurant('Лилипут1', 'Детская1', 2)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.change_the_rating(new)
restaurant2.change_the_rating(new1)