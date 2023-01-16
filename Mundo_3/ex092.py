import datetime
from datetime import date
dados = dict()
ano = int(0)
ano = datetime.date.today()
ano = ano.year
dados = {'nome': str(input('Nome: ')).strip(), 'ano_nasc': int(input('Ano de Nascimento: ')),
        'ctps': int(input('Carteira de Trabalho ["0" para não tem]: '))}
idade = ano - dados['ano_nasc']
if dados["ctps"] == 0:
    print('-----------------------------------------------------')
    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {idade} anos')
    print('DADOS INSUFICIENTES PARA O CÁLCULO DE APOSENTADORIA!')
    print('-----------------------------------------------------')
else:
    dados['ano_contrato'] = int(input('Ano de Contratação: '))
    dados['sal'] = float(input('Salário: R$ '))
    ano_aposent = dados['ano_contrato'] + 35
    idade_aposent = ano_aposent - dados['ano_nasc']
    print('-----------------------------------------------------')
    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {idade} anos')
    if idade_aposent > idade:
        print(f'Você se aposentará com {idade_aposent} anos.')
    elif idade_aposent == idade:
        print(f'Você se aposentará esse ano.')
    else:
        print(f'Você já deveria ter se aposentado há {idade - idade_aposent} anos.')
    print('-----------------------------------------------------')

