print('\033[7m#\033[m' * 19)
print('\033[7m# \033[1m\033[4mMAIOR OU MENOR?\033[m\033[7m #\033[m')
print('\033[7m#\033[m' * 19)
print(' ')
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
if n1 > n2:
    print('O \033[31mprimeiro valor\033[m é \033[34mmaior\033[m.')
elif n2> n1:
    print('O \033[31msegundo valor\033[m é \033[34mmaior\033[m.')
else:
    print('\033[31mNão existe\033[m valor maior, os dois são \033[34miguais\033[m.')
