soma = 0
cont = 0
print('-=' * 30)
print('{:^60}'.format(' SOMA DE ÍMPARES MÚLTIPLOS DE 3 '))
print('-=' * 30)
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A somatória entre todos os {} ímpares múltiplos de 3 é: {}'.format(cont, soma))
