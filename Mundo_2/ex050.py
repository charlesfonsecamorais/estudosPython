s = int(0)
cont = 0
n = int(0)
for c in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    cont = cont + 1
    if (n % 2) == 0:
        s = s + n
print('Você informou {} números e a somatório de todos os números pares informados é: {}'.format(cont, s))
