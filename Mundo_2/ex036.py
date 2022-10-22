from time import sleep
print('\033[0;32m-=-\033[m' * 20)
print('\033[1;34mSIMULADOR DE FINANCIAMENTO\033[m')
print('\033[0;32m-=-\033[m' * 20)
casa = float(input('Informe o valor do imovel que deseja financiar: R$ '))
sal = float(input('Informe o seu salário atual: R$ '))
anos = int(input('Informe o tempo de financiamento (em anos): '))
prestacao = float(casa / (anos * 12))
if prestacao <= (sal * 30 / 100):
    print('Para comprar o imóvel no valor de {}, você pagará uma prestação de R$ {:.2f}'.format(casa, prestacao))
    print('Processando sua solicitação: AGUARDE...')
    sleep(5)
    print('\033[1;36mPARABÉNS, SEU FINANCIAMENTO FOI APROVADO!!!\033[m')
else:
    print('Para comprar o imóvel no valor de R$ {:.2f}, você pagará uma prestação de R$ {:.2f}'.format(casa, prestacao))
    print('Processando sua solicitação: AGUARDE...')
    sleep(5)
    print('\033[1;31m"SEU FINANCIAMENTO FOI REPROVADO! CONSULTE O SEU GERENTE DE CONTAS"\033[m')
