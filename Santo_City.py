city = str(input('Informe o nome de sua cidade: ')).strip()
#city[:5].upper() == 'SANTO'
#cidade = city.split()
#print('A cidade começa com o nome "SANTO"?', 'Santo' in cidade[0])
print('\033[3mA cidade começa com o nome "SANTO"?\033[m', city[:5].upper() == 'SANTO')
