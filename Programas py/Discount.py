print('\033[41m \033[m' * 22)
p = float(input('Preço do produto: R$'))
print('\033[41m \033[m' * 22)
print(' ' * 20)
pd = p - p * 5 / 100
print('\033[1;41mCom desconto, seu produto passa a custar R${:.2f}.\033[m'.format(pd))
