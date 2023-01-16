from time import sleep
a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
pa = a1
cont = 0
termos = 10
views = 1
while views != 0:
    while cont < termos:
        print('{}'.format(pa), end=' '),
        pa = pa + r
        cont = cont + 1
    print('', end='\n')
    print('Deseja ver mais quantos termos?')
    views = int(input('Digite a sua resposta: '))
    if views > 0:
        termos = termos + views
print('A progressão terminou com {} termos apresentados!'.format(termos))
sleep(2)
print('ENCERRANDO...')
sleep(3)
print('-=-=-=-=-=-=-=-=-=-= FIM =-=-=-=-=-=-=-=-=-=-')