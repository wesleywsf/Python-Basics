r1 = float(input('Informe, em cm, o tamanho da primeira reta: '))
r2 = float(input('Informe, em cm, o tamanho da segunda reta: '))
r3 = float(input('Informe, em cm, o tamanho da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo ', end = '')
    if r1 == r2 == r3:
        print('\033[34mEQUILÁTERO\033[m com essas retas.')
    elif r1 != r2 != r3 != r1:
        print('\033[34mESCALENO\033[m com essas retas.')
    else:
        print('\033[34mISÓCELES\033[m com essas retas.')
else:
    print('Não é possível formar um triângulo com essas retas.')
