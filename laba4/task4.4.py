count = input("Введите номер билета: ")
l = int(len(count) / 2)
a = int(count[:l])
b = int(count[l:])
sum1 = 0
sum2=0
sum = 0
while (a != 0):
    sum1 = sum1 + (a % 10)
    a = a // 10
while (b != 0):
    sum2 = sum2 + (b % 10)
    b = b // 10
if sum1==sum2:
    print("Это счастливый билет")
else:
    print("Это не счастливый билет")