enru = {}
with open('C:\\Users\\user\\PycharmProjects\\Algorit\\laba10\\en-ru.txt', 'r') as file:
    for line in file:
        en, ru = line.strip().split(' - ')

        ru = ru.strip().split(', ')

        for i in ru:
            if i not in enru:
                enru[i] = [en]
            else:
                enru[i].append(en)

enru = sorted(enru.items())
print(enru)
with open('C:\\Users\\user\\PycharmProjects\\Algorit\\laba10\\ru-en.txt', 'w') as file:
    st = ''
    for i in enru:
        s2 = f'{i[0]} - {", ".join(i[1])}'
        st += s2 + '\n'
    print(st)
    file.write(st)
