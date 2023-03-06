word=input('Введите слово: ')
for i in word:
    if "ф" or "Ф" in word:
        print('Ого! Вы ввели редкое слово!')
        break
    else:
        print('Эх, это не очень редкое слово...')
        break
