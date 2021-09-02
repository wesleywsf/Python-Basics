n1 = float(input('Insira sua nota do 1º Semestre: '))
n2 = float(input('Insira sua nota do 2º Semestre: '))
med = (n1 + n2) / 2
print('Média = {:.2f}'.format(med))
if med < 5.0:
    print('\033[1;31mREPROVADO\033[m')
elif 5.0 <= med < 7.0:
    print('\033[1;34mRECUPERAÇÃO\033[m')
else:
    print('\033[1;32mAPROVADO\033[m')