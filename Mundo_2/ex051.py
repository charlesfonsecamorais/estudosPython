a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
a10 = a1 + (10 - 1) * r
for c in range(a1, a10 + r, r):
    print('{}'.format(c), end=' ')
