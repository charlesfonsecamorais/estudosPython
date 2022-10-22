times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atlético-MG',
         'Santos', 'América=MG', 'Goiás', 'Bragantino', 'Fortaleza', 'São Paulo', 'Botafogo', 'Ceará-SC', 'Coritiba',
         'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')
cinco = times[0:5]
ultimos = times[-4:]
alfa = sorted(times)
goias = (times.index('Goiás')) + 1
print('{:^30}'.format('CAMPEONATO BRASILEIRO 2022'))
print('{}'.format('=' * 30))
print(f'Os cinco primeiros colocados na tabela são: {cinco}')
print(f'Os lanternas do brasileirão são: {ultimos}')
print(f'Lista com os times em ordem alfabética:')
print(f'{alfa}')
print(f'O Goiás está em {goias} lugar na tabela.')


