viagem = float(input('Qual a distância da sua viagem em km? '))
preco = viagem*0.45 if viagem > 200 else viagem*0.5
print('Sua passagem vai custar R${:.2f}.'.format(preco))
