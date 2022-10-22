num = int(0)
val = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o valor {c}: '))
    if num % 2 == 0:
        val[0].append(num)
        val[0].sort()
    else:
        val[1].append(num)
        val[1].sort()
print('=' * 50)
print(f'Os valores pares digitados foram: {val[0]}')
print(f'Os valores ímpares digitados foram: {val[1]}')
