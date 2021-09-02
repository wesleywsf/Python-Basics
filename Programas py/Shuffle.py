from random import shuffle
n1 = str(input('\033[7;40mPrimeiro aluno:\033[m ')).strip()
n2 = str(input('\033[40mSegundo aluno:\033[m ')).strip()
n3 = str(input('\033[7;40mTerceiro aluno:\033[m ')).strip()
n4 = str(input('\033[40mQuarto aluno:\033[m ')).strip()
lista = [n1, n2, n3, n4]
shuffle(lista)
print('\033[7;40mA ordem de apresentação será:\033[m ')
print('\033[7;30;42m\033[3m', lista, '\033[m')
