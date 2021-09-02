from math import sin, cos, tan, radians
n = float(input('Informe um ângulo: '))
s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))
print('O \033[4mseno\033[m de {:.0f}º é \033[40m{:.2f}\033[m, o \033[4mcosseno\033[m é \033[40m{:.2f}\033[m e o \033[4mtangente\033[m é \033[40m{:.2f}\033[m.'.format(n, s, c, t))
