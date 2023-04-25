import json

with open('C:/Users/user/PycharmProjects/Algorit/laba10/laba100.json', 'r') as file:
    read = file.read() #читаем файл строку
loadstr = json.loads(read) #СТРОЧКУ ПРЕОБРАЗОВЫВАЕМ В СЛОВАРЬ
#print(repr(loadstr))
while True:
    que = input('Хотите добавить новую запись?Да/Нет ')
    if que == 'Да':
        name = input("Ведите название ")
        price = int(input("Ведите цену "))
        available = input("Ведите в наличии или нет.Да/Нет ")
        if available == "Да":
            available = True
        else:
            available = False
        weight = int(input("Ведите вес "))
        new = {'name': name, 'price': price, 'available': available, 'weight': weight}
        loadstr.get('products').append(new)
        with open('C:/Users/user/PycharmProjects/Algorit/laba10/laba10.json', 'w') as file:
            file.write(json.dumps(loadstr, indent=4)) #преобрз словарь в строчку


    elif que == "Нет":
        break

for i in loadstr.get('products'):
    print(f"Название: {i.get('name')}")
    print(f"Цена: {i.get('price')}")
    print(f"Вес: {i.get('weight')}")
    if i.get('available'):
        print('В наличии')
    else:
        print('Нет в наличии!')
