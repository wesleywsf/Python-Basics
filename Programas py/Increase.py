sal = float(input('Salário atual: R$'))
aum = sal + sal * 15 / 100
print('\033[1;30;43mCom aumento de 15%, seu salário será de R${:.2f}.\033[m'.format(aum))
