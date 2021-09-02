print('\033[1;30;43m+-------------+\033[m')
print('\033[1;30;43m| Cálculo IMC |\033[m')
print('\033[1;30;43m+-------------+\033[m')
print(' ')
peso = float(input('Qual o seu peso em kg? '))
altura = int(input('Qual a sua altura em cm? '))
imc = peso / (altura / 100) ** 2
print('Seu IMC é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')
