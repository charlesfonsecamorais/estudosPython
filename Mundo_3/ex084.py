princ = []
temp = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        print('RESPOSTA INVÁLIDA! TENTE NOVAMENTE.')
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('-' * 30)
print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso cadastrado foi {mai}Kg de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso cadastrado foi {men}Kg de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end=' ')
print()
print(f'-' * 30)
