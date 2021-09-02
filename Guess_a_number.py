from random import choice
from time import sleep
lista = [0, 1, 2, 3, 4, 5]
num = choice(lista)
print('#'* 37)
print('# Vou pensar em um número de 0 a 5. #')
print('#' * 37)
print('LOADING...')
sleep(2)
escolha = int(input('Qual você acha que foi? '))
if escolha == num:
    print('ACERTÔ MIZERÁVI!')
else:
    print('ERRROOOUU!!!')
print('O número secreto era o {}.'.format(num))
