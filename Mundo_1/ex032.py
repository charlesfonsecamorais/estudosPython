from datetime import date
ano = int(input('Digite o ano que deseja consultar (Digite "0" para consultar o ano atual): '))
if ano == 0:
    ano = date.today().year
data = (ano // 1) % 100
if (data % 4) == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é um ano BISSEXTO'.format(ano))
else:
    print('O ano de {} não é um ano BISSEXTO'.format(ano))
