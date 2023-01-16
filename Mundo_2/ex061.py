a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
pa = a1
cont = 0
while cont < 10:
    print('{} '.format(pa), end=(''))
    pa = pa + r
    cont = cont + 1
print('FIM')