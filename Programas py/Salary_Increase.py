sal = float(input('Qual é o seu salário atual? R$'))
if sal > 1250:
    sal = sal + (10 / 100 * sal)
else:
    sal = sal + (15 / 100 * sal)
print('Seu salário, com aumento, passará a ser de R${:.2f}.'.format(sal))
