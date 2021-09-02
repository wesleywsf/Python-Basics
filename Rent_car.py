d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = (d * 60) + (0.15 * km)
print('\033[1m\033[7;40mO total a pagar é de R${:.2f}.\033[m'.format(total))
