soma = n = cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n <= 998:
        soma += n
        cont += 1
    else:
        break
print(f'A soma dos {cont} números digitados foi {soma}')
