from random import randint
aposta = ''.strip().upper()
parouimpar = ''
computador = randint(0, 10)
vitorias = 0
cont = 1
print('{}'.format('-=') * 15)
print('{:^30}'.format('PAR OU ÍMPAR'))
print('{}'.format('-=') * 15)
while cont > 0:
    jogador = int(input('Digite um número: '))
    aposta = str(input('Escolha Par ou Ímpar [P/I]: ')).strip().upper()[0]
    if aposta != 'P' and aposta != 'I':
        print('OPÇÃO INVÁLIDA!!!')
        aposta = str(input('Escolha Par ou Ímpar [P/I]? ')).strip().upper()[0]
    elif (jogador + computador) % 2 == 0:
        parouimpar = 'P'
    else:
        parouimpar = 'I'
    if aposta == parouimpar:
        print('Parabéns!!! Você venceu!!!')
        print('Vamos continuar nosso jogo!!!')
        cont += 1
        vitorias += 1
    else:
        break
if aposta == 'P':
    print(f'GAME OVER! Você digitou {jogador} e o computador escolheu {computador}')
    print('O resultado foi ÍMPAR!!!')
else:
    print(f'GAME OVER! Você digitou {jogador} e o computador escolheu {computador}')
    print('O resultado foi PAR!!!')
print(f'Você jogou {cont} vezes e venceu {vitorias} vezes do Computador.')
