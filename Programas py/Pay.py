print('{:*^40}'.format(' DOIT TECH '))
price = float(input('Qual é o preço do produto? R$'))
print('''Qual a condição de pagamento?
[ 1 ] Dinheiro/Cheque à vista
[ 2 ] Crédito à vista 
[ 3 ] Crédito em 2x 
[ 4 ] Crédito em 3x ou mais''')
opt = int(input('Sua opção: '))
if opt == 1:
    total = price - (price * 10 / 100)
    print('Nessa forma de pagamento você ganha \033[1;34m10% de desconto\033[m.')
elif opt == 2:
    total = price - (price * 5 / 100)
    print('Nessa forma de pagamento você ganha \033[1;33m5% de desconto\033[m.')
elif opt == 3:
    total = price
    parc = total / 2
    print('Nessa forma de pagamento você não ganha desconto. Cada parcela irá custar R${:.2f}.'.format(parc))
elif opt == 4:
    total = price + (price * 20 / 100)
    parc = int(input('Em quantas parcelas quer dividir? '))
    print('Nessa forma de pagamento haverá \033[1;31mjuros de 20%\033[m no valor total do seu produto.')
    print('A compra será parcelada em {}x de R${:.2f}.'.format(parc, total / parc))
else:
    total = price
    print('\033[1;31mOPERAÇÃO INVÁLIDA. PROCESSO ENCERRADO.\033[m')
print('Seu produto vai custar R${:.2f} ao final.'.format(total))
