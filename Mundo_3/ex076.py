print('{}'.format('-') * 50)
print('{:^50}'.format('LISTA DE PREÇOS'))
print('{}'.format('-') * 50)
produto = ('Mochila', 79.90, 'Caderno', 14.75, 'Lápis', 1.25, 'Borracha', 2.50, 'Caneta', 7.00)
for posicao in range(0, len(produto)):
    if posicao % 2 == 0:
        print(f'{produto[posicao]:.<44}', end='')
    else:
        print(f'{produto[posicao]:>6}')
