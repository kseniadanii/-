res=""

while True:
    word = input("Введите слово: ")

    if word == "stop":

        break
    res = res + word+" "
print("Конец программы: ", res.strip())
