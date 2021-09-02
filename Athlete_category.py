from datetime import date
ano = date.today().year
nasc = int(input('Informe o ano de nascimento do(a) atleta: '))
idade = ano - nasc
print('Atleta com {} anos.'.format(idade))
cat = ano - nasc
if cat <= 9:
    print('Categoria: \033[1;34mMIRIM\033[m')
elif 9 < cat <= 14:
    print('Categoria: \033[1;34mINFANTIL\033[m')
elif 14 < cat <= 19:
    print('Categoria: \033[1;34mJUNIOR\033[m')
elif 19 < cat <= 25:
    print('Categoria: \033[1;34mSÊNIOR\033[m')
else:
    print('Categoria: \033[1;34mMASTER\033[m')
