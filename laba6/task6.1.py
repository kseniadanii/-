dictionary = {'Россия': 'Москва', 'Бельгия': 'Брюссель', 'Великобритания': 'Лондон', 'Япония': 'Токио',
              'Франция': 'Париж'}

for (k, v) in dictionary.items():
    print(k, '-', v)
print('\n')
print("Сортировка:")
print(*sorted(dictionary), sep=',')
print('\n')
country = input("Введите страну: ")

if country not in dictionary:
    print("Неверная страна!")
else:
    print('Столица', country.replace('я', 'и'), "-", dictionary[country])
