valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor inserido com sucesso!')
    else:
        print('VALOR DUPLICADO! O valor digitado será descartado:')
    r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if r not in 'SN':
        print('Resposta Incorreta!')
        r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    elif r == 'N':
        break
valores.sort()
print(f'Os valores digitados foram: {valores}')
