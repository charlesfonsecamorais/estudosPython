from time import sleep
boletim = [[], [], [], []]
result = nome = ''
n1 = n2 = media = 0
while True:
    nome = str(input('Nome: ')).strip()
    boletim[0].append(nome)
    n1 = float(input('{}'.format('Nota 1: ')))
    boletim[1].append(n1)
    n2 = float(input('{}'.format('Nota 2: ')))
    boletim[2].append(n2)
    media = (n1 + n2) / 2
    boletim[3].append(media)
    result = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while result not in 'SN':
        print('Resposta Inválida!!!')
        result = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if result == 'N':
        break
print('=' * 25)
print('COD.', end=' ')
print('ALUNO', end=' ')
print('{:>12}'.format('MÉDIA'))
print('=' * 25)
for c in range(0, len(boletim[0])):
    print(f' {c}', end='   ')
    print(f'{boletim[0][c]:<10}', end='     ')
    print(f'{boletim[3][c]}')
while True:
        print('-' * 25)
        notas = int(input('Deseja mostrar as notas de qual aluno? (999 para FINALIZAR): '))
        print('-' * 25)
        if notas != 999:
            print(f'As notas de {boletim[0][notas]} são: ', end='')
            print(f'{boletim[1][notas]} e ', end='')
            print(f'{boletim[2][notas]}')
        else:
            break
print('Finalizando...')
sleep(3)
print(' <<< Até breve >>>!!!')
