valores = list()
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor da posição {c}: ')))
    maior = max(valores)
    menor = min(valores)
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor digitado foi: {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi: {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')


