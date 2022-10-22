par = tuple
v = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Os números digitados foram: {v}')
print('O número "9" foi digitado {} vezes.'.format(v.count(9)))
if 3 in v:
    print('O número "3" aparece na posição: {}'.format(v.index(3) + 1))
else:
    print(f'O número "3" não aparece em {v}')
print('Os números pares digitados foram: ', end='')
for c in range(0, 4):
    if v[c] % 2 == 0:
        par = (v[c])
        print(f'{par}, ', end='')
