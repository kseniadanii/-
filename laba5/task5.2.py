spisok1 = [10, 4, 6, 8, 3, 5, 5, 10, 7, 8]

print(spisok1)
x = ''
for i in range(len(spisok1) - 1):
    for j in range(i + 1, len(spisok1)):
        if spisok1[i] == spisok1[j]:
            x = x + str(spisok1[i]) + " "
print("Повторяющиеся элементы:", x)
