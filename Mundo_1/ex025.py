nome = str(input('Digite o seu nome completo: ')).strip()
silva = 'SILVA' in nome.upper()
if silva == True:
    result = 'Sim'
else:
    result = 'Não'
print('Existe "Silva" no nome? {}'.format(result))
