from datetime import date
ano = date.today().year
nasc = int(input('Informe seu ano de nascimento: '))
if (ano - nasc) < 18:
    print('Falta(m) {} ano(s) para seu alistamento no serviço militar.'.format(18 - (ano - nasc)))
elif (ano - nasc) > 18:
    print('Você deveria ter se alistado {} ano(s) atrás.'.format((ano - nasc) -18))
else:
    print('{} é o ano em que você deve se alistar no serviço militar.'.format(ano))
