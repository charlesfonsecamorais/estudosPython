expressao = str('')
aberto = fechado = 0
expressao = str(input('Digite uma expressão [use parênteses "( )]": '))
if '(' in expressao:
    aberto = expressao.count('(')
if ')' in expressao:
    fechado = expressao.count(')')
if aberto != fechado or aberto == fechado == 0:
    print('Expressão inválida!')
elif expressao.index(')') < expressao.index('('):
    print('Expressão inváida!')
else:
    print('Expressão válida! Parabéns!')
