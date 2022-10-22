aluno = dict()
aluno = {'nome': str(input('Nome: ')).strip(),
         'media': float(input(f'Média: '))
         }
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(f'Nome do aluno: {aluno["nome"]}')
print(f'Média do aluno: {aluno["media"]}')
print(f'Situação do aluno: {aluno["situacao"]}')
