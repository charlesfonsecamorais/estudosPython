n = int(0)
r = str('')
listagem = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    listagem.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while r not in 'SN':
        print('RESPOSTA INVÁLIDA!!!')
        r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
listagem.sort()
print(f'Os números digitados foram: {listagem}')
pares.sort()
print(f'Os números pares digitados foram: {pares}')
impares.sort()
print(f'Os números ímpares digitados foram: {impares}')
