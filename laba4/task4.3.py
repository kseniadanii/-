date = input("Введите дату формата 'xx.yy.zzzz': ")
res_date = date.replace('.', '')

l = int(len(res_date) / 2)

b = int(res_date[6:])
x1 = int(res_date[:2])
x2 = int(res_date[2:4])

if x1 * x2 == b:
    print(True)

else:
    print(False)
