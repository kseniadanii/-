a = 100


def division(count):
    return a % count != 0


count = input("Введите число: ")
try:
    val = int(count)
except ValueError:
    print("Нужно ввести число!")
if count == '0':
    print("Делить на ноль нельзя!")
else:
    print(a // int(count))
