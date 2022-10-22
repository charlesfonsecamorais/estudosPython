n1 = (input('Digite o primeiro número: '))
n2 = (input(' Digite o segundo número: '))
n3 = (input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    maior = n1
else:
    if n2 > n1 and n2 > n3:
        maior = n2
    else:
        maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
else:
    if n2 < n1 and n2 < n3:
        menor = n2
    else:
        menor = n3
print('O maior número digitado foi: {}'.format(maior))
print('O menor número digitado foi: {}'.format(menor))
