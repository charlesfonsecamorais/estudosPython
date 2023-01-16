from datetime import date
from time import sleep
ano = date.today().year
print('\033[;33m_-\033[m' * 20)
print('\033[1;32mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('\033[;33m-_\033[m' * 20)
data = int(input('Informe o ano de seu nascimento para verificarmos a sua categoria: '))
cat = (ano - data)
if data > ano:
    print('DATA INCORRETA! VERIFIQUE A DATA E DIGITE NOVAMENTE.')
elif cat <= 9:
    print('Pesquisando: Aguarde...')
    sleep(2)
    print('Sua idade atual é {} anos.'.format(cat))
    print('A sua categoria é \033[1;35mMIRIM')
elif cat <= 14:
    print('Pesquisando: Aguarde...')
    sleep(2)
    print('Sua idade atual é {} anos.'.format(cat))
    print('A sua categoria é \033[1;35mINFANTIL')
elif cat <= 19:
    print('Pesquisando: Aguarde...')
    sleep(2)
    print('Sua idade atual é {} anos.'.format(cat))
    print('A sua categoria é \033[1;35mJUNIOR')
elif cat <= 20:
    print('Pesquisando: Aguarde...')
    sleep(2)
    print('Sua idade atual é {} anos.'.format(cat))
    print('A sua categoria é \033[1;35mSÊNIOR')
else:
    print('Pesquisando: Aguarde...')
    sleep(2)
    print('Sua idade atual é {} anos'.format(cat))
    print('A sua categoria é \033[1;35mMASTER')
