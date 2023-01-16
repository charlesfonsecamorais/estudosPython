frase = str(input('Digite uma frase qualquer: ')).strip()
up = frase.upper()
a = up.count('A')
print('A letra "A" foi digitada {} vezes na frase!'.format(a))
print('Ela aparece pela primeira vez na letra {}'.format(up.find('A')+1))
print('Ela aparece pela última vez na letra {}'.format(up.rfind('A')+1 - (up.count(' '))))

