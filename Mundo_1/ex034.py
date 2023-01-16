sal = float(input('Digite o valor do seu salário para calcular o reajuste: R$ '))
if sal > 1250:
    print('O seu novo salário será de R$ {:.2f}'.format(sal * 1.1))
else:
    print('O seu novo salário será de R$ {:.2f}'.format(sal * 1.15))
