idade = maiores = homens = mulheres = 0
c = 1
sexo = ''
continuar = ''
while c != 0:
    print('{}'.format('-=') * 20)
    print('CADASTRO {}'.format(c))
    idade = int(input('Digite a idade: '))
    while idade < 0:
        idade = int(input('Digite a idade: '))
    if idade > 18:
        maiores += 1
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
    else:
        c += 1
print('')
print(f'Total de cadastros efetuados: {c}')
print(f'Maiores de 18 anos: {maiores}')
print(f'Homens: {homens} ')
print(f'Mulheres menores de 20 anos: {mulheres}')
print('')
print('-=-=-=-=-=-=-=-=-=-= FIM =-=-=-=-=-=-=-=-=-=-')