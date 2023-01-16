from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=' * 20)
print('{:^40}'.format('JOGOS DA MEGA SENA'))
print('-=' * 20)
quant = int(input('Quantos jogos deseja que eu sorteie?: '))
total = 1
while total <= quant:
    cont = 0
    while True:
        sorteio = randint(1, 60)
        if sorteio not in lista:
            lista.append(sorteio)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)