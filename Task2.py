# Создайте программу для игры с конфетами человек против человека.
# a) Добавьте игру против бота

import random

print('Не останься последним! ')

sweets = 2021

corch = random.randint(0,1)

while sweets > 0:
    if corch == 1:
        sweets -= int(input('Сколько заберете конфет? '))
        print('осталось: ', sweets)

        corch = 0
    else:
        comp = random.randint(1, sweets%28)
        sweets -= comp
        print('Компьютер забрал', comp)
        print('Осталось конфет: ', sweets)

        corch = 1

if corch == 0:
    print('Человек проиграл')
elif corch == 1:
    print('Человек победил')