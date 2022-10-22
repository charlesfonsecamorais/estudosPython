a = float(input('Informe o primeiro segmento de reta: '))
b = float(input(' Informe o segundo segmento de reta: '))
c = float(input('Informe o terceiro segmento de reta: '))
abc = a + b + c
if a > b and a > c:
    maior = a
elif b > c and b > a:
    maior = b
else:
    maior = c
#regra para validar a existência de um triângulo
if abc - maior <= maior:
    print('\033[1;31mNão é possível construir um TRIÂNGULO com esses segmentos de reta!\033[m')
#regra para definir um triângulo equilátero
elif a == b and b == c:
    print('Com esses segmentos formamos um \033[1;33mTRIÂNGULO EQUILÁTERO\033[m')
#regra para definir um triângulo isóceles
elif a == b and a != c or b == c and b != a or a == c and a != b:
    print('Com esses segmentos formamos um \033[1;33mTRIÂNGULO ISOCELES\033[m')
else:
    print('Com esses segmentos formamos um \033[1;33mTRIÂNGULO ESCALENO\033[m')
