import random

group1 = ['Иванов', 'Котов', 'Сидоров', 'Лебедев', 'Дятлов', 'Кузнецов', 'Богданов', 'Любимеин', 'Пупкин', 'Лолкин']
group2 = ['Чугунова', 'Овчинникова', 'Емельянова', 'Киселёва', 'Яковлева', 'Байол', 'Киреева', 'Пискунова', 'Шашкин']
team = tuple(random.sample(group1, 5) + random.sample(group2, 5))


print("Изначальный список:\n",group1,"\n", group2,"\n")
print("Новый кортеж:\n", team,"\n")

print("Длина: ", len(team),'\n')
team = tuple(sorted(list(team)))
print("Сортировка: \n", team,"\n")

if "Иванов" in team:
    print("Иванов встречается", list(team).count("Иванов"), "раз")
else:
    print("Иванов не встречается в кортеже")
