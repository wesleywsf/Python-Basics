c = float(input('Informe a temperatura em ºC: '))
f = c * 9 / 5 + 32
print('\033[1;34mA temperatura de {:.1f}ºC corresponde a {:.1f}ºF!\033[m'.format(c, f))
