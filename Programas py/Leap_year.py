from datetime import date
ano = int(input('Que ano deseja saber se é bissexto? (Escolha "0" para o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
"""if ano % 4 == 0:
    if ano % 100 != 0:
        print('O ano {} é bissexto.'.format(ano))
    else:
        if ano % 400 == 0:
            print('O ano {} é bissexto.'.format(ano))
        else:
            print('O ano {} não é bissexto.'.format(ano))
else:
    if ano % 400 == 0:
        print('O ano {} é bissexto.'.format(ano))
    else:
        print('O ano {} não é bissexto.'.format(ano))"""
