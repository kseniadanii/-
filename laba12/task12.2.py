class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Название {self.restaurant_name} ')
        print(f'Тип кухни {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} открыт')


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, location, schedule, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.location = location
        self.schedule = schedule
        self.flavors = flavors

    def print_flavors(self):
        for flavor in self.flavors:
            print(flavor)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print('Вкус добавлен')

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print('Вкус удален')
        else:
            print("Такого вкуса нет!")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print('Такой вкус есть!')
        else:
            print('Такого вкуса нет!')


class SoftIceCream(IceCreamStand):
    def mix(self):
        print('Мороженое смешиавется')


class Popsicle(IceCreamStand):
    def sort(self):
        print('Эскимо расскладывается на витрину')


rest1 = IceCreamStand('Мороз', 'Кафе-Мороженое', 'Санкт-Петербург', '10:00 - 22:00', ['Клубника', 'Шоколад', 'Ваниль'])
rest3 = IceCreamStand('Моро1з', 'Кафе-Мороженое1', 'Санкт-Петербург1', '10:001 - 22:00', ['Клубниа', 'Шокол1ад', 'Ванил1ь'])
rest1.describe_restaurant()
rest1.print_flavors()
rest1.add_flavor(input('Введите вкус для добавления: '))
rest1.check_flavor(input('Какой вкус проверить в наличии? '))
rest1.remove_flavor(input('Введите вкус для удаления: '))
rest1.print_flavors()

rest2 = SoftIceCream('Мороз', 'Кафе-Мороженое', 'Санкт-Петербург', '10:00 - 22:00', ['Клубника', 'Шоколад', 'Ваниль'])
rest2.mix()
rest2 = Popsicle('Мороз', 'Кафе-Мороженое', 'Санкт-Петербург', '10:00 - 22:00', ['Клубника', 'Шоколад', 'Ваниль'])
rest2.sort()

rest2.check_flavor(input('Введите'))