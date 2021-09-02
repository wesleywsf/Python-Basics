from random import choice
from time import sleep
print('{:=^15}'.format(' JOKENPÔ '))
print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
opt = int(input('Sua escolha: '))
jkp = [1, 2, 3]
escolha = choice(jkp)
print('{: ^15}'.format(' JO '))
sleep(0.6)
print('{: ^15}'.format(' KEN '))
sleep(0.6)
print('{: ^17}'.format(' PÔ!!! '))
if opt == 1 and escolha == 2:
    print('Você escolheu \033[1;31mPEDRA\033[m e eu escolhi \033[1;34mPAPEL\033[m.')
    print('Papel embrulha pedra, EU GANHEI!!!')
elif opt == 1 and escolha == 3:
    print('Você escolheu \033[1;34mPEDRA\033[m e eu escolhi \033[1;31mTESOURA\033[m.')
    print('Pedra quebra Tesoura, VOCÊ GANHOU!!!')

elif opt == 2 and escolha == 3:
    print('Você escolheu \033[1;31mPAPEL\033[m e eu escolhi \033[1;34mTESOURA\033[m.')
    print('Tesoura corta papel, EU GANHEI!!!')
elif opt == 2 and escolha == 1:
    print('Você escolheu \033[1;34mPAPEL\033[m e eu escolhi \033[1;31mPEDRA\033[m.')
    print('Papel embrulha pedra, VOCÊ GANHOU!!!')

elif opt == 3 and escolha == 1:
    print('Você escolheu \033[1;31mTESOURA\033[m e eu escolhi \033[1;34mPEDRA\033[m.')
    print('Pedra quebra Tesoura, EU GANHEI!!!')
elif opt == 3 and escolha == 2:
    print('Você escolheu \033[1;34mTESOURA\033[m e eu escolhi \033[1;31mPAPEL\033[m.')
    print('Tesoura corta papel, VOCÊ GANHOU!!!')

elif opt == escolha:
    print('Deu EMPATE! Nós dois escolhemos ', end = '')
    if opt == 1:
        print('\033[1;33mPEDRA\033[m! Kkkk')
    elif opt == 2:
        print('\033[1;33mPAPEL\033[m! Kkkk')
    else:
        print('\033[1;33mTESOURA\033[m! Kkkk')

else:
    print('\033[1;31mOPÇÃO INVÁLIDA! JOGO ENCERRADO.\033[m')

#from random import randint
# from time import sleep
# itens = ('Pedra', 'Papel', 'Tesoura')
# computador = randint(0,2)
# print('O computador escolheu {}'.format(itens[computador]))
# print('''Suas opções:
# [ 0 ] PEDRA
# [ 1 ] PAPEL
# [ 2 ] TESOURA''')
# jogador = int(input('Qual é a sua jogada? '))
# print('JO')
# sleep(1)
# print('KEN')
# sleep(1)
# print('PO!!!')
# print('-=' * 11)
# print('Computador jogou {}'.format(itens[computador]))
# print('Jogador jogou {}'.format(itens[jogador]))
# print('-=' * 11)
# if computador == 0: # computador jogou PEDRA
#     if jogador == 0:
#         print('EMPATE')
#     elif jogador == 1:
#         print('JOGADOR VENCE')
#     elif jogador == 2:
#         print('COMPUTADOR VENCE')
#     else:
#         print('JOGADA INVÁLIDA!')
# elif computador == 1: # computador jogou PAPEL
#     if jogador == 0:
#         print('COMPUTADOR VENCE')
#     elif jogador == 1:
#         print('EMPATE')
#     elif jogador == 2:
#         print('JOGADOR VENCE')
#     else:
#         print('JOGADA INVÁLIDA!')
# elif computador == 2: # computador jogou TESOURA
#     if jogador == 0:
#         print('JOGADOR VENCE')
#     elif jogador == 1:
#         print('COMPUTADOR VENCE')
#     elif jogador == 2:
#         print('EMPATE')
#     else:
#         print('JOGADA INVÁLIDA!')