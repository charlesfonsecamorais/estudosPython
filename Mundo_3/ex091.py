from random import randint
from time import sleep
dados = mai = men = 0
jogador = dict()
ranking = list()
print('------ SORTEIO ------')
sleep(1)
for c in range(1, 5):
    dados = randint(1, 6)
    jogador = {'numero': c,
               'sorteio': dados
               }
    if c == 1:
        mai = men = jogador['sorteio']
        ranking.append(jogador['numero'])
        ranking.append(jogador['sorteio'])
    if jogador['sorteio'] > mai:
        mai = jogador['sorteio']
        ranking.insert(0, jogador['sorteio'])
        ranking.insert(0, jogador['numero'])
    if jogador['sorteio'] < men:
        men = jogador['sorteio']
        ranking.append(jogador['numero'])
        ranking.append(jogador['sorteio'])
    print(f'O jogador {jogador["numero"]} tirou {jogador["sorteio"]}')
    jogador.clear()
    sleep(1)
print()
print('------ RANKING ------')
sleep(1)
print()
for c in range(0, 4):
    print(f'{(c+1)}º lugar: ', end='')
    print()
    sleep(1)
