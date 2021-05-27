t = int(input())

lines = []
for _ in range(t):
    itens = [int(grade) for grade in input().split()]

    ovnis = int(itens[0]) + int(itens[1])
    plataforma = itens[2]
    uniform = plataforma >= ovnis

    lines.append('CABE!' if uniform else 'NAO CABE!')

print('\n'.join(lines), end='')
