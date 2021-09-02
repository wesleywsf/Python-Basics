v = float(input('A quantos km/h estava o carro? '))
if v <= 80:
    print('Obrigado, tenha uma boa viagem.')
else:
    multa = (v-80)*7
    print('Você foi multado em R${:.2f} por excesso de velocidade!'.format(multa))
