maior = 0
menor = 0
media = 0
soma = 0
cont = 1
resp = ''.upper()
valor = int(input('Digite um número qualquer: '))
while resp != 'N':
    soma = soma + valor
    if valor > maior:
        maior = valor
    else:
        menor = valor
    resp = str(input('Deseja digitar outro número? [S/N]: ').upper())
    if resp == 'S':
        valor = int(input('Digite um novo número: '))
        cont += 1
media = float(soma / cont)
print('A média entre todos os números digitados foi de {:.2f}'.format(media))
print('O MAIOR número digitado foi o {}.'.format(maior))
print('O MENOR número digitado foi o {}.'.format(menor))
