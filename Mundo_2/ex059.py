from time import sleep
menu = 0
adicao = 0
mult = 0
maior = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while menu != 5:
    print('''
    \033[1;33m[1]\033[m \033[1;34msomar\033[m
    \033[1;33m[2]\033[m \033[1;34mmultiplicar\033[m
    \033[1;33m[3]\033[m \033[1;34mmaior\033[m
    \033[1;33m[4]\033[m \033[1;34mnovos números\033[m 
    \033[1;33m[5]\033[m \033[1;34msair do programa\033[m
    ''')
    menu = int(input('DIGITE A OPÇÃO DESEJADA: '))
    if menu == 1:
        adicao = n1 + n2
        print('{} + {} = {}'.format(n1, n2, adicao))
    elif menu == 2:
        mult = n1 * n2
        print('{} X {} = {}'.format(n1, n2, mult))
    elif menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor digitado foi {}'.format(maior))
    elif menu == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif menu >= 6:
        print('OPÇÃO INVÁLIDA!!! DIGITE NOVAMENTE:')
print('O programa está sendo encerrado.')
print('{}'.format('AGUARDE'), end='')
sleep(1)
print('{}'.format('.'), end='')
sleep(1)
print('{}'.format('.'), end='')
sleep(1)
print('{}'.format('.'))
sleep(1)
print(' ')
print('\033[1;32m{}\033[m'.format('-------------- FIM --------------'))
