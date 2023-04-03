number = int(input("Введите количество слов: "))
res=""
for i in range(0,number):
    word=input("Введите слово: ")
    res=res+word
    if i != number-1:
        res=res+ " "
print("Результат:" , res)





