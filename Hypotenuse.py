from math import pow, sqrt, hypot
ca = float(input('\033[4m\033[1;45mInforme o valor do cateto adjacente:\033[m '))
co = float(input('\033[4m\033[1;46mInforme o valor do cateto oposto:\033[m '))
#hip = sqrt((pow (ca, 2)+pow(co, 2)))
hip = hypot(ca, co)
print('\033[1m\033[4;47mNesse triângulo, a hipotenusa é igual a \033[41m {:.2f}.\033[m'.format(hip))
