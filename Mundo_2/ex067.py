from time import sleep
m = 0
c = n = 1
print('{}'.format('~') * 30)
print('{:^30}'.format('Conheça a TABUADA'))
print('{}'.format('~') * 30)
while n > 0:
    c = 1
    n = int(input('Digite um número: '))
    for c in range(1, 11):
        if n > 0:
            m = n * c
            print(f'{n} X {c} = {m}')
            c += 1
        else:
            break
print('O programa será finalizado!')
sleep(2)
print('AGUARDE...')
sleep(3)
print('{:~^30}'.format('FIM'))



