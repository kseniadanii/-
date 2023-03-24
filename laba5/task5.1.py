a=[1,3,12,10,4]
user_input=int(input("Введите число: "))
if user_input in a:
    print(a)
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")