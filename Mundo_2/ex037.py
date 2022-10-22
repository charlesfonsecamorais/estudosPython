n = int(input('Digite um número qualquer para conversão: '))
print('-=-'*15)
print('- Digite \033[1;34m1\033[m para \033[1;33mBINÁRIO\033[m')
print('- Digite \033[1;34m2\033[m para \033[1;33mOCTAL\033[m')
print('- Digite \033[1;34m3\033[m para \033[1;33mHEXADECIMAL\033[m')
print('-=-'*15)
escolha = int(input('Digite a opção desejada: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a: {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a: {}'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a: {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida!')
