summ = 0
with open('C:/Users/user/PycharmProjects/Algorit/laba9/laba9.3.csv', 'r') as file:
    next(file)
    print("Нужно купить:")
    for i in file:
        product, count, price = i.strip().split(',')
        sum0 = (int(count) * int(price))
        summ += sum0
        print(f'{product} - {count} шт. за {price} руб.')
    print(f'Итоговая сумма: {summ} руб.')