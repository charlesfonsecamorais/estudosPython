nome = input('Digite o seu nome: ')
peso = float(input('Informe o seu peso (Kg): '))
altura = float(input('Informe a sua altura (m): '))
imc = peso/altura**2
print('{}, o seu IMC é: {:.2f}'.format(nome, imc))


