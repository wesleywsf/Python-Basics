print('\033[7;33m*\033[m' * 39)
print('\033[1m\033[7;33m AVALIAÇÃO PARA EMPRÉSTIMO RESIDENCIAL \033[m')
print('\033[7;33m*\033[m' * 39)
print(' ')
casa = float(input('Qual o valor da residência que deseja financiar? R$'))
sal = float(input('Qual o valor mensal do seu salário? R$'))
prazo = int(input('Durante quantos anos deseja pagar? '))
mensal = casa / prazo / 12
print('A prestação vai ficar R${:.2f}/mensais.'.format(mensal))
print('Essa prestação \033[4multrapassa\033[m 30% do seu salário, seu empréstimo foi \033[1;31mNEGADO\033[m.' if mensal > sal * 30 / 100 else 'Essa prestação não ultrapassa 30% do seu salário, seu empréstimo foi \033[1m\033[4;34mLIBERADO\033[m!')
