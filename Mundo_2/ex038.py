print('-_' * 20)
print('\033[1;33mCOMPARAÇÃO NUMÉRICA\033[m')
print('-_' * 20)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('{} é maior do que {}'.format(n2, n1))
else:
    print('Não há um valor maior, os números digitados são iguais.')
