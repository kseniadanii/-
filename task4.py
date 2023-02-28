color1=input("Цвет 1: ")
color2=input("Цвет 2: ")
a="Красный"
b="Синий"
c="Желтый"
if color1 not in (a,b,c) or color2 not in (a,b,c):
    print("Ошибка!")
else:
    if (color1==a and color2==b) or (color2==a and color1==b):
        print("Фиолетовый")
    if (color1==a and color2==c) or (color2==a and color1==c) :
        print("Оранжевый")
    if (color1==b and color2==c) or (color2==b and color1==c):
        print("Зеленый")
    if color1==color2:
        print(color1)