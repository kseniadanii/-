import json

with open('C:/Users/user/PycharmProjects/Algorit/laba10/laba100.json', 'r') as file:
    read = file.read()
loadstr = json.loads(read)
#print(repr(loadstr))

for i in loadstr.get('products'):
    print(f"Название: {i.get('name')}")
    print(f"Цена: {i.get('price')}")
    print(f"Вес: {i.get('weight')}")
    if i.get('available'):
        print('В наличии')
    else:
        print('Нет в наличии!')


