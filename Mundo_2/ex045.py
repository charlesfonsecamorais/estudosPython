import random
from time import sleep
print('\033[;33m-_\033[m' * 30)
print('\033[1;32m{:^56}\033[m'.format('DESAFIO'))
print('\033[;33m-_\033[m' * 30)
print('''- (1) PEDRA
- (2) PAPEL
- (3) TESOURA''')
print('\033[;33m-_\033[m' * 30)
escolha = ('pedra', 'papel', 'tesoura')
pc = random.choice(escolha)
gamer = int(input('ESCOLHA A SUA OPÇÃO E BOA SORTE!!! => '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if gamer == 1 and pc == 'pedra':
    print('PEDRA X PEDRA: EMPATE!')
elif gamer == 1 and pc == 'papel':
    print('PEDRA X PAPEL: VOCÊ PERDEU!')
elif gamer == 1 and pc == 'tesoura':
    print('PEDRA X TESOURA: VOCÊ VENCEU!')
elif gamer == 2 and pc == 'pedra':
    print('PAPEL X PEDRA: VOCÊ VENCEU!')
elif gamer == 2 and pc == 'papel':
    print('PAPEL X PAPEL: JOGUE NOVAMENTE!')
elif gamer == 2 and pc == 'tesoura':
    print('PAPEL X TESOURA: VOCÊ PERDEU!')
elif gamer == 3 and pc == 'pedra':
    print('TESOURA X PEDRA: VOCÊ PERDEU!')
elif gamer == 3 and pc == 'papel':
    print('TESOURA X PAPEL: VOCÊ VENCEU!!')
else:
    print('TESOURA X TESOURA: JOGUE NOVAMENTE!')
