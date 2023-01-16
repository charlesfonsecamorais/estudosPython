from datetime import date
ano = date.today().year
data = 0
maior = 0
menor = 0
erro = ''
for c in range(0, 7):
    data = int(input('Digite a data do seu nascimento: '))
    if (ano - data) >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('De acordo com as datas fornecidas, {} pessoas já atingiram a maioridade e {} pessoas ainda são menores de idade.'.format(maior, menor))
