nome = str(input('Digite o seu nome completo: ')).strip()
'''divisao = nome.split()
cont = (int(len(divisao)) - 1)
primeiro = divisao[0]
ultimo = divisao[cont]
print('Primeiro nome: {}'.format(primeiro))
print('Último nome: {}'.format(ultimo))'''
div = nome.split()
print('Olá, {}! É um prazer te conhecer!'.format(nome))
print('O seu primeiro nome é: {}'.format(div[0]))
print('O seu último nome é: {}'.format(div[len(div)-1]))

