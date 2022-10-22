from time import sleep
print('{:-^50}'.format(' \033[1;33mTABUADA\033[m '))
n = int(input('Digite um número para conhecer a sua TABUADA: '))
for c in range(1, 11, 1):
    op = n * c
    print('-' * 12)
    print('{} X {:>2} = {:>2}'.format(n, c, op))
    sleep(0.5)
