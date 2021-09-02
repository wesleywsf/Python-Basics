frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra "A" (sem acento) aparece \033[7;43m{}\033[m vez(es) na sua frase.'.format(frase.count('a')))
print('A \033[7;43mprimeira\033[m vez que ela aparece é como o {}º caractere da frase.'.format(frase.find('a')+1))
print('A \033[7;43múltima\033[m vez que ela aparece é como o {}º caractere da frase.'.format(frase.rfind('a')+1))
