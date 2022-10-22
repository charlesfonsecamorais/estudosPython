from datetime import date
from time import sleep
print('\033[33m-\033[m\033[32m_\033[m' * 10)
print('\033[33mALISTAMENTO MILITAR\033[m')
print('\033[33m-\033[m\033[32m_\033[m' * 10)
ev = date.today().year
print('''
    Informe o seu sexo:
    [1] para Masculino
    [2] para Feminino
    ''')
sexo = int(input('Digite a sua opção: '))
if sexo == 2:
    print('Você não tem obrigação de se alistar.')
    print('Para maiores informações, procure a junta militar mais próxima.')
elif sexo == 1:
    nasc = int(input('Informe o ano de seu nascimento: '))
    if nasc > ev:
        print('\033[1;31mData incorreta. Favor verificar a data digitada.\033[m')
    elif (ev - nasc) > 18:
        data = (ev - nasc) - 18
        print('Processando seus dados: AGUARDE...')
        sleep(2)
        print(
            '\033[1;31mVocê deveria ter se alistado {} anos atrás. Procure imediatamente a junta militar.\033[m'.format(
                data))
    elif (ev - nasc) < 18:
        data = 18 - (ev - nasc)
        print('Processando seus dados: AGUARDE...')
        sleep(2)
        print('\033[1;33mFalta(m) {} ano(s) para o seu alistamento. Não se esqueça!\033[m'.format(data))
    else:
        print('Processando seus dados: AGUARDE...')
        sleep(2)
        print('\033[1;32mVocê deve procurar a junta militar imediatamente. Chegou a hora de se alistar!\033[m')
