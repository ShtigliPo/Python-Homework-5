# Создайте программу для игры в ""Крестики-нолики"".

import random
def check_x(pole):
    if pole[0][0] == 'x' and pole[1][1] and pole[2][2] == 'x':
        print('x wins')
        return True
    elif pole[2][0] == 'x' and pole[1][1] == 'x' and pole[0][2] == 'x':
        print('x wins')
        return True
    elif pole[0][0] == 'x' and pole[0][1] == 'x' and pole [0][2] == 'x':
        print('x wins')
        return True
    elif pole[0][0] == 'x' and pole[1][0] == 'x' and pole[2][0] == 'x':
        print('x wins')
        return True
    elif pole[2][0] == 'x' and pole[2][1] == 'x' and pole [2][2] == 'x':
        print('x wins')
        return True
    elif pole[0][2] == 'x' and pole[1][2] == 'x' and pole[2][2] == 'x':
        print('x wins')
        return True
    else:
        return False

def check_o(pole):
    if pole[0][0] == 'O' and pole[1][1] == 'O' and pole[2][2] == 'O':
        print('O wins')
        return True
    elif pole[2][0] == 'O' and pole[1][1] == 'O' and pole[0][2] == 'O':
        print('O wins')
        return True
    elif pole[0][0] == 'O' and pole[0][1] == 'O' and pole [0][2] == 'O':
        print('O wins')
        return True
    elif pole[0][0] == 'O' and pole[1][0] == 'O' and pole[2][0] == 'O':
        print('O wins')
        return True
    elif pole[2][0] == 'O' and pole[2][1] == 'O' and pole [2][2] == 'O':
        print('O wins')
        return True
    elif pole[0][2] == 'O' and pole[1][2] == 'O' and pole[2][2] == 'O':
        print('O wins')
        return True
    else:
        return False

pole = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_']]
for i in pole:
    print(i)

while not check_x(pole) and not check_o(pole):
    a, b = int(input()), int(input())
    pole[a][b] = 'x'
    for i in pole:
        print(i)
    print('Ход компьютера')
    while True:
        c, d = random.randint(0,2), random.randint(0,2)
        if pole[c][d] == '_':
            break
    pole[c][d] = 'O'
    for i in pole:
        print(i)
            
