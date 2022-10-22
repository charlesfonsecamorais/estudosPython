km = float(input('Digite a velocidade em Km/h: '))
if km > 80:
    print('Você ultrapassou o limite de velocidade permitido que é de 80km/h!')
    print('O valor da multa a ser pago é de R$ {:.2f}'.format((km-80) * 7))
else:
    print('Você está no limite de velocidade permitido! Boa viagem!!!')
