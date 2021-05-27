p = input().split(' ')

x = int(p[0])
y = int(p[1])

if x == 0:
    if y == 0:
        print('NO ALVO!', end='')
if x > 0:
    if y > 0:
        print('R1', end='')
    if y < 0:
        print('R4', end='')
if x < 0:
    if y < 0:
        print('R3', end='')
    if y > 0:
        print('R2', end='')
