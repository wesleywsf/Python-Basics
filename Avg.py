n1 = float(input('Nota 1º sem.: '))
n2 = float(input('Nota 2º sem.: '))
mid = (n1 + n2) / 2
print('Sua média este ano foi \033[1;30;41m{}\033[m'.format(mid) if mid < 7 else 'Sua média este ano foi \033[1;30;42m{}\033[m'.format(mid))
