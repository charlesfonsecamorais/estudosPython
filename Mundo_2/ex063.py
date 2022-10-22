n = 0
print('-=' * 30)
print('{:^60}'.format(' FIBONACCI '))
print('-=' * 30)
n = int(input('Quantos termos deseja mostrar?: '))
t1 = 0
t2  = 1
cont = 3
print('{} - {} '.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print('- {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' {}'.format('FIM'))
