n1 = input()

s1 = input()

n2 = input()

s2 = input()

n3 = input()

calc = (n1 + s1 + n2 + s2 + n3)


def calcular(calc):
    print(int(eval(calc)), end='')


try:
    calcular(calc)
except ZeroDivisionError:
    print('erro')
