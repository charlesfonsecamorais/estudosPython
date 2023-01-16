jogadores = list()
jogador = dict()
gols = list()
result = ''
while True:
    print('------------------------------------------')
    jogador = {'nome': str(input('Nome: ')).strip(), 'partidas': int(input('Nº de partidas: '))}
    for p in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na {p+1}ª partida?: ')))
    jogador['saldo'] = sum(gols)
    result = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while result not in 'SN':
        print('Resposta Inválida! Tente novamente.')
        result = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if result in 'nN':
        break
