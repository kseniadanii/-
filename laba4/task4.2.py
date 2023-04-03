a = 100


def division(count):
    return a % count != 0


count = input("Введите число: ")
try:
    val = int(count)
except ValueError:
    print("Нужно ввести число!")
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
print(a // int(count))
