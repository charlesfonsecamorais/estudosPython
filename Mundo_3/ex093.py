jogador = dict()
gols = list()
saldo = 0
jogador = {'nome': str(input('Nome: ')).strip(),
           'partidas': int(input('Nº de partidas: '))
           }
for p in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols na {p+1}ª partida?: ')))
    saldo += gols[p]
print('-----------------------------------------------')
print(f'Jogador: {jogador["nome"]}')
print(f'Nº de partidas jogadas: {jogador["partidas"]}')
print(f'Saldo de gols na temporada: {saldo}')
print('-----------------------------------------------')
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas na temporada.')
for p, g in enumerate(gols):
    print(f'Na {p+1}ª partida, fez {g} gols')
