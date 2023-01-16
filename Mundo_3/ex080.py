lista = []
n = 0
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0:
        lista.append(n)
        print('Adicionado no final da lista...')
    elif c == 1:
        if n < lista[0]:
            lista.insert(0, n)
            print('Adicionado na posição 0 da lista')
        else:
            lista.append(n)
            print('Adicionado na posição 1 da lista...')
    elif c == 2:
        if n < lista[0]:
            lista.insert(0, n)
            print('Adicionado na posição 0 da lista')
        elif lista[0] < n <= lista[1]:
            lista.insert(1, n)
            print('Adicionado na posição 1 da lista...')
        else:
            lista.append(n)
            print('Adicionado na posição 2 da lista...')
    elif c == 3:
        if n < lista[0]:
            lista.insert(0, n)
            print('Adicionado na posição 0 da lista')
        elif lista[0] < n <= lista[1]:
            lista.insert(1, n)
            print('Adicionado na posição 1 da lista...')
        elif lista[1] < n <= lista[2]:
            lista.insert(2, n)
            print('Adicionado na posição 2 da lista...')
        else:
            lista.append(n)
            print('Adicionado na posição 3 da lista')
    elif c == 4:
        if n < lista[0]:
            lista.insert(0, n)
            print('Adicionado na posição 0 da lista')
        elif lista[0] < n <= lista[1]:
            lista.insert(1, n)
            print('Adicionado na posição 1 da lista...')
        elif lista[1] < n <= lista[2]:
            lista.insert(2, n)
            print('Adicionado na posição 2 da lista...')
        elif lista[2] < n <= lista[3]:
            lista.insert(3, n)
            print('Adicionado na posição 3 da lista...')
        else:
            lista.append(n)
            print('Adicionado na posição 4 da lista...')
print(f'Os números digitados foram: {lista}')
