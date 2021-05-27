valor = input().split(' ')
a = int(valor[0])
b = int(valor[1])
c = int(valor[2])

m1 = (a + b + abs(a - b)) // 2
m2 = (c + m1 + abs(m1 - c)) // 2

print(m2, end='')
