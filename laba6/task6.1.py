dictionary = {'Россия': 'Москва', 'Бельгия': 'Брюссель', 'Великобритания': 'Лондон', 'Япония': 'Токио',
              'Франция': 'Париж'}
for (k, v) in dictionary.items():
    print(k, '-', v)
country = input("Введите страну: ")
if country not in dictionary:
    print("Неверная страна!")
else:
    print(country, " - ", dictionary[country])
print(sorted(dictionary))
