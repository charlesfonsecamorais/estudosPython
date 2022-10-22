n = int(0)
r = str('')
lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while r not in 'SN':
        print('ERRO! Digite novamente.')
        r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}', end='')
if 5 in lista:
    print(f'\n O número "5" foi digitado {lista.count(5)} vez(es)')
else:
    print('\n O número "5" não foi digitado.')
print('{}'.format('-=') * 20)
