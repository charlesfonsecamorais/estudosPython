print('-=' * 25)
print('{:^50}'.format('Números primos'))
print('-=' * 25)
n = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont = cont + 1
if cont == 2:
    print('O número \033[33m{}\033[m é um número PRIMO!'.format(n))
else:
    print('O número \033[31m{}\033[m NÃO É um número PRIMO!'.format(n))
