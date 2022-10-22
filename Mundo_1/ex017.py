from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite 0 comprimento do cateto adjacente: '))
hi = hypot(co, ca)
'''A soma dos quadrados dos catetos é igual ao quadrado da hipotenusa'''
print('O valor da hipotenusa é: {:.2f}'.format(hi))
