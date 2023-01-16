palavras = ('Aprender', 'Programar', 'Python', 'Migracao', 'Carreira', 'Futuro')
for cont in palavras:
    print(f'\nA palavra {cont.upper()} tem as vogais: ', end='')
    for letra in cont:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end='')
