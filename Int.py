from math import trunc
n = float(input('Digite um número: '))
i = trunc(n)
print('O número {} tem a parte inteira \033[4;41m{}\033[m.'.format(n, i ))
