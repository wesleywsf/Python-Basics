a = int(input('Insira um número: '))
b = int(input('Insira outro número: '))
c = int(input('Insira mais um número: '))
maior = a
menor = a
if b > maior:
    maior = b
if c > maior:
    maior = c
if b < menor:
    menor = b
if c < menor:
    menor = c
print('O maior número é o {} e o menor é o {}.'.format(maior, menor))
