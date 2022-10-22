from random import randint
computador = randint(0, 10)
gamer = 0
contador = 0
print('\033[;34m-=\033[m' * 50)
print('\033[;33m{:^100}\033[m'.format(' DESCUBRA O NÚMERO PENSADO PELO COMPUTADOR E VENÇA O DESAFIO!!!'))
print('\033[;34m-=\033[m' * 50)
print('DIGITE UM NÚMERO DE 0 A 10')
while computador != gamer:
    gamer = int(input('FAÇA A SUA APOSTA: '))
    contador += 1
    if computador > gamer:
        print('Mais...')
    elif computador < gamer:
        print('Menos...')
print('\033[;34m-=\033[m' * 22)
print('PARABÉNS, VOCÊ ACERTOU!')
print('Você precisou de {} tentativas para acertar!'.format(contador))
print('\033[;34m-=\033[m' * 22)
