media = float(0)
soma = 0
nmvelho = str('').strip()
idvelho = 0
nova = int(0)
for cont in range(1, 5):
    print('-=' * 12)
    print('CADASTRO {}'.format(cont))
    print('-=' * 12)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M / F): ')).strip().upper()
    soma = soma + idade
    media = soma / 4
    if sexo == 'M':
        if idade > idvelho:
            idvelho = idade
            nmvelho = nome
    elif sexo == 'F':
        if idade < 20:
            nova = nova + 1
print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(idvelho, nmvelho))
print('Ao todo são {} mulheres com menos de 20 anos no grupo.'.format(nova))
