l = float(input('Qual a largura da sua parede (em metros)? '))
h = float(input('Qual a altura da sua parede (em metros)? '))
a = l * h
t = a / 2
print('\033[3;40mSua parede tem {:.2f}m² de área e precisará de {:.0f}l de tinta para ser pintada.\033[m'.format(a, t))
