n = int(input('Informe um número que deseje converter: '))
print("""Escolha uma das bases para conversão:
\033[32m[ 1 ]\033[m converter para \033[31mBINÁRIO\033[m
\033[32m[ 2 ]\033[m converter para \033[34mOCTAL\033[m
\033[32m[ 3 ]\033[m converter para \033[33mHEXADECIMAL\033[m""")
opt = int(input('\033[32mSua opção:\033[m '))
if opt == 1:
    print('{} convertido para \033[31mBINÁRIO\033[m é igual a {}'.format(n, bin(n)[2:]))
elif opt == 2:
    print('{} convertido para \033[34mOCTAL\033[m é igual a {}'.format(n, oct(n)[2:]))
elif opt == 3:
    print('{} convertido para \033[33mHEXADECIMAL\033[m é igual a {}'.format(n, hex(n)[2:]))
else:
    print('\033[1;30;42m Opção inválida. Tente novamente. \033[m')
