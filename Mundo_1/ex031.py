print('-=-' * 20)
km = float(input('Digite a distância (em Km) que deseja percorrer:  '))
print('-=-' * 20)
if km <= 200:
    print('O valor da passagem é: R$ {:.2f} '.format(km * 0.5))
else:
    print('O valor da passagem é: R$ {:.2f}'.format(km * 0.45))
