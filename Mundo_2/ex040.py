a1 = float(input('Digite a primeira nota: '))
a2 = float(input(' Digite a segunda nota: '))
media = (a1 + a2) / 2
if media >= 7.0:
    print('Sua média final foi {:.1f}'.format(media))
    print('PARABÉNS, VOCÊ FOI APROVADO!')
elif media >= 5:
    print('Sua média final foi {:.1f}'.format(media))
    print('VOCÊ ESTÁ DE RECUPERAÇÃO. ESTUDE PARA A SUA PROVA!')
else:
    print('Sua média final foi {:.1f}'.format(media))
    print('VOCÊ FOI REPROVADO!')
