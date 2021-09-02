n = int(input('Digite um número: '))
print('O \033[1;30;41mdobro\033[m de {} é {}, o \033[4;30;41mtriplo\033[m é {} e a \033[1m\033[4;30;41mraiz quadrada\033[m é {:.2f}.'.format(n, n*2, n*3, n**(1/2)))
