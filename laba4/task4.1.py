def is_division(count):
    return count % 3 == 0


count = int(input("Введите число: "))
if is_division(count):
    print("Yes")
else:
    print("No")
