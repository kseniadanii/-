from tkinter import *


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors


rest1 = IceCreamStand('Мороз', 'Кафе-Мороженое', ['Клубника', 'Шоколад', 'Ваниль'])

root = Tk()

root['bg'] = '#FFC0CB'
root.geometry('150x100')
#Не дает изменять окно вручную
root.resizable(width=False, height=False)
title = Label(text='Вкусы:')
#Размещает текст в окне
title.pack()
stroke = rest1.flavors
stroke_var = Variable(value=stroke)
#listbox просматривает список однострочных текстовых элементов
stroke_listbox = Listbox(listvariable=stroke_var)
stroke_listbox.pack()
root.mainloop()
