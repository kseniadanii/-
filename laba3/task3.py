word=input('Введите слово: ')

for i in word:
    if (i=="ф" ) or (i=="Ф"):
        print('Ого! Вы ввели редкое слово!')
        break
    else:
        print('Эх, это не очень редкое слово...')
        break
