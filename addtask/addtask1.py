import random

# Открываем файл с синонимами и создаем словарь
synonyms = {}
with open('synonyms.txt', 'r') as f:
    for line in f:
        word, syns = line.strip().split(' - ')
        synonyms[word] = syns.split('; ')

# Запрашиваем у пользователя слово для замены
word = input('Введите слово для замены: ')

# Если слово есть в словаре, выбираем случайный синоним и заменяем слово
if word in synonyms:
    syn = random.choice(synonyms[word])
    print(f'Заменяем "{word}" на "{syn}"')
else:
    # Если слова нет в словаре, предлагаем пользователю внести свой вариант
    print(f'Слово "{word}" не найдено в словаре')
    new_syn = input('Введите свой вариант синонима: ')
    synonyms[word] = [new_syn]
    with open('synonyms.txt', 'a') as f:
        f.write(f'\n{word} - {new_syn}')
