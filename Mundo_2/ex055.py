maior = 1
menor = 0
for cont in range(1, 6):
    peso = float(input('Digite o seu peso: '))
    if peso > maior and maior > menor:
        maior = peso
    else:
        menor = peso
print('o maior peso digitado foi {:.1f} Kg'.format(maior))
print('o menor peso digitado foi {:.1f} Kg'.format(menor))
