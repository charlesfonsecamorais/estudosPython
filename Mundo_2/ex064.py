valor = 0
soma = 0
cont = 0
while valor <= 998:
        valor = int(input('Digite um numero [999 para encerrar]: '))
        if valor <= 998:
            soma = soma + valor
            cont += 1
print('Foram digitados {} números e a soma deles é: {}.'.format(cont, soma))
