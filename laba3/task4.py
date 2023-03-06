count=0
win=0
while True:
    import random
    random_number1 = random.randint(0, 10)
    random_number2 = random.randint(0, 10)

    res=int(input(str(random_number1) + ' + ' + str(random_number2) + ' = '))
    if random_number1 + random_number2 == res:
        print("Правильно!")
        win+=1
    else:
        print("Ответ неверный")
        count+=1
        if count==3:
            print("Игра окончена. Правильных ответов: ", win)
            break


