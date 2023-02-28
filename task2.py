nomer = int(input("Введите номер места: "))
is_valid = 1 <= nomer <= 54
is_up = (nomer % 2) == 0
is_side = 36 <= nomer <= 55
if not is_valid:
    print("Неверные данные!")
else:
    print("Информация о месте:")
    if is_up and is_side:
        print("Верхнее боковое")
    if is_up and not is_side:
        print("Верхнее купе")
    if not is_up and is_side:
        print("Нижнее боковое")
    if not is_up and not is_side:
        print("Нижнее купе")
