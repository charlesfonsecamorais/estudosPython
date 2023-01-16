m1 = float(input('Digite a primeira medida em cm: '))
m2 = float(input(' Digite a segunda medida em cm: '))
m3 = float(input('Digite a terceira medida em cm: '))
if m1 > m2 and m1 > m3:
    maior = m1
else:
    if m2 > m1 and m2 > m3:
        maior = m2
    else:
        maior = m3
calc = (m1 + m2 + m3) - maior
if calc <= maior:
    print('Os segmentos de reta {}, {} e {} não podem formar um Triângulo'.format(m1, m2, m3))
else:
    print('Os segmentos de reta {}, {} e {} podem formar um Triângulo!'.format(m1, m2, m3))
