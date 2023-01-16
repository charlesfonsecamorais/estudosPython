p = float(input('Digite o preço do produto: R$ '))
desc = p * 0.05
vp = p - desc
print('O desconto aplicado foi de R$ {} e você pagará apenas R$ {:.2f}'.format(desc, vp))
