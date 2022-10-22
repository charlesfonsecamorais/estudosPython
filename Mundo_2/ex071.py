cinquenta = vinte = dez = um = 0
resto = 1
print('=' * 50)
print('{:^50}'.format('BANCO 24 HORAS'))
print('=' * 50)
valor = int(input('Digite o valor que deseja sacar: R$ '))
while resto != 0:
    if valor >= 50:
        cinquenta = valor // 50
        resto = valor - (cinquenta * 50)
        if resto >= 20:
            vinte = resto // 20
            resto = resto - (vinte * 20)
        if resto >= 10:
            dez = resto // 10
            resto = resto - (dez * 10)
        if resto >= 1:
            um = resto // 1
            resto = resto - (um * 1)
    elif valor >= 20:
        vinte = valor // 20
        resto = valor - (vinte * 20)
        if resto >= 10:
            dez = resto // 10
            resto = resto - (dez * 10)
        if resto >= 1:
            um = resto // 1
            resto = resto - (um * 1)
    elif valor >= 10:
        dez = valor // 10
        resto = valor - (dez * 10)
        if resto >= 1:
            um = resto // 1
            resto = resto - (um * 1)
    elif valor >= 1:
        um = valor // 1
        resto = valor - (um * 1)
print(f'Notas de R$ 50: {cinquenta}')
print(f'Notas de R$ 20: {vinte}')
print(f'Notas de R$ 10: {dez}')
print(f'Notas de R$  1: {um}')
