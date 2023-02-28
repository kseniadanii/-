def is_leap_year(year):
    return (year%4==0 and  year%100!=0) or year%400==0
year=int(input("Введите год: "))
if is_leap_year(year):
    print("Год ", year , "- високосный")
else:
    print("Этот год не високосный")
