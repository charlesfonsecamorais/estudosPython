from time import sleep
print('\033[33m#\033[m' * 50)
print('\033[1;32mCALCULADORA DE IMC\033[m')
print('\033[33m#\033[m' * 50)
nome = str(input('Digite o seu nome: ')).strip()
peso = float(input(' Informe o seu peso (Kg): '))
altura = float(input('Informe a sua altura (m): '))
imc = peso/altura**2
if imc < 18.5:
    print('Calculando, aguarde...')
    sleep(2)
    print('{}, o seu IMC atual é de {:.1f} e você está \033[1;33mABAIXO DO PESO.'.format(nome, imc))
elif imc < 25:
    print('Calculando, aguarde...')
    sleep(2)
    print('{}, o seu IMC atual é de {:.1f} e você está no \033[1;33mPESO IDEAL.'.format(nome, imc))
elif imc < 30:
    print('Calculando, aguarde...')
    sleep(2)
    print('{}, o seu IMC atual é de {:.1f} e você está com \033[1;33mSOBREPESO.'.format(nome, imc))
elif imc < 40:
    print('Calculando, aguarde...')
    sleep(2)
    print('{}, o seu IMC atual é de {:.1f} e você está com \033[1;33mOBESIDADE.'.format(nome, imc))
else:
    print('Calculando, aguarde...')
    sleep(2)
    print('{}, o seu IMC atual é de {:.1f} e você está com \033[1;33mOBESIDADE MÓRBIDA.'.format(nome, imc))
