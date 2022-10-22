lg = float(input('Digite a largura da área que deseja pintar (m): '))
alt = float(input('Digite a altura da área que deseja pintar (m): '))
area = lg * alt
tinta = area / 2
print('A área a ser pintada tem {:.2f} metros quadrados'.format(area))
print('Você precisará de {:.1f} litros de tinta para pintá-la'.format(tinta))

