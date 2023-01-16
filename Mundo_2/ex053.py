print('+' * 50)
print('{:^50}'.format('PALÍNDROMOS'))
print('+' * 50)
frase = str(input('Digite uma frase: ')).strip().upper()
uniao = ''.join(frase.split())
cont = len(uniao)
inversao = ''
for c in range(cont - 1, -1, -1):
   inversao = inversao + uniao[c]
if uniao == inversao:
    print('A frase {} invertida fica {}, portanto temos um PALÍNDROMO!'.format(uniao, inversao))
else:
    print('A frase {} invertida fica {}, portanto não temos um PALÍNDROMO!'.format(uniao, inversao))
