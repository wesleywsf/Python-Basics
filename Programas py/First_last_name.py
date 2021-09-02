nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('Seu primeiro nome é \033[1;34m{}\033[m'.format(n[0]))
print('Seu último nome é: \033[1;36m{}\033[m'.format(n[len(n)-1]))
