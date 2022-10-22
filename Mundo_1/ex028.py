from random import randint
from time import sleep
r = randint(0, 5) # faz o PC "escolher" um número de 0 à 5
n = int(input('Digite um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(2)
if n > 5:
    print('O número digitado é inválido!!!')
else:
    if n == r:
        print('=--' * 12)
        print('Parabéns, você acertou em cheio!!!')
        print ('=--' * 12)
    else:
        print('Que pena, você errou! Tente novamente!')
        print('O número sorteado era o {}'.format(r))
