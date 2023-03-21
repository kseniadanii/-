date=input("Введите дату формата 'xx.yy.zzzz': ")
res_date = date.replace('.', '')
print(res_date)
sum1=1
l = int(len(res_date) / 2)
a = int(res_date[:l])
b = int(res_date[6:])
x1=int(res_date[:2])
x2=int(res_date[2:4])
print(x1, x2,b)
if x1*x2==b:
    print(True)

else:
    print(False)
