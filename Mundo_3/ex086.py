matriz = [[], [], []]
n = 0
for v in range(0, 3):
        n = int(input(f'Digite um valor para [0, {v}]: '))
        matriz[0].append(n)
for v in range(0, 3):
        n = int(input(f'Digite um valor para [1, {v}]: '))
        matriz[1].append(n)
for v in range(0, 3):
        n = int(input(f'Digite um valor para [2, {v}]: '))
        matriz[2].append(n)
print('{}'.format('-=') * 15)
print(f'[  {matriz[0][0]}  ]', end='  ')
print(f'[  {matriz[0][1]}  ]', end='  ')
print(f'[  {matriz[0][2]}  ]', end='  ')
print(f'\n[  {matriz[1][0]}  ]', end='  ')
print(f'[  {matriz[1][1]}  ]', end='  ')
print(f'[  {matriz[1][2]}  ]', end='  ')
print(f'\n[  {matriz[2][0]}  ]', end='  ')
print(f'[  {matriz[2][1]}  ]', end='  ')
print(f'[  {matriz[2][2]}  ]')
print('{}'.format('-=') * 15)
