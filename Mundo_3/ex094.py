dados = dict()
cadastro = list()
mulheres = list()
idade_acima = list()
idade = media = 0
cont = 0
result = ''
while True:
    cont += 1
    dados['nome'] = str(input('Nome: ')).split()
    dados['sexo'] = str(input('Sexo [M/F]: ')).split()[0]
    while dados['sexo'] not in 'mMfF':
        print('Resposta Inválida!')
        dados['sexo'] = str(input('Sexo [M/F]: '))
    if dados['sexo'] in 'fF':
        mulheres.append(dados['nome'].copy())
    dados['idade'] = int(input('Idade: '))
    idade += dados['idade']
    media = idade / cont
    cadastro.append(dados.copy())
    result = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while result not in 'SN':
        print('Resposta inválida!')
        result = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if result == 'N':
        break
print(f'Foram cadastradas {cont} pessoas.')
print(f'A média de idade do grupo é de {media:.2f} anos.')
print(f'As mulheres cadastradas são: {mulheres}')


