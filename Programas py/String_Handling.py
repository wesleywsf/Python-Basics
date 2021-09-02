nome = str(input('Digite seu nome completo: ')).strip()
primeiro = nome.split()[0]
print('Com todas as letras maiúsculas seu nome fica assim: \033[1m\033[7;41m {} \033[m'.format(nome.upper()))
print('Com todas as letras minúsculas, fica assim: \033[1;30;42m {} \033[m'.format(nome.lower()))
print('No total, seu nome possui \033[4m{}\033[m letras.' .format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem \033[1m\033[3m{}\033[m letras.'.format(len(primeiro)))
