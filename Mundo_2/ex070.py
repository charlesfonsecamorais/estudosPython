produto = continuar = nomebarato = ''
preco = precobarato = precocaro = caros = total = 0
c = 1
while c != 0:
    print('{}'.format('-=') * 20)
    print('{} - PRODUTO {}'.format('CARRINHO DE COMPRAS', c))
    print('{}'.format('-=') * 20)
    produto = str(input('PRODUTO: ')).strip().upper()
    preco = float(input('PREÇO: R$ '))
    total += preco
    if c == 1:
        precocaro = precobarato = preco
        nomebarato = produto
    elif preco >= precocaro:
        precocaro = preco
    else:
        precobarato = preco
        nomebarato = produto
    if preco > 1000:
        caros += 1
    continuar = str(input('DESEJA CONTINUAR COMPRANDO [S/N]: ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('DESEJA CONTINUAR COMPRANDO [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
    c += 1
print('')
print(f'Produtos comprados: {c}')
print(f'Valor total da compra: R$ {total:.2f}')
print(f'Produtos que custaram mais de R$ 1.000: {caros}')
print(f'Produto mais barato: {nomebarato}')
