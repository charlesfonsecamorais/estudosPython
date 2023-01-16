dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos quilômetros rodados? '))
vt = dias * 60 + km * 0.15
print('O valor a total a ser pago é de R$ {:.2f} '.format(vt))
