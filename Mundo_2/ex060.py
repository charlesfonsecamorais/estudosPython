print('-=' * 20)
print('{:^40}'.format('FATORIAL'))
print('-=' * 20)
n = int(input('Digite um valor para calcular o seu Fatorial: '))
c = n
f = 1
print('Calculando {}!: '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    f = f * c
    c = c - 1
print(f)