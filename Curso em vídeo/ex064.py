print('Digite para essa soma somente numeros inteiros, e para pausar digite um float')
n = float(input('Digite o primeiro número da soma: '))
s = 0
i = 1
while n%1 == 0:
    s = s + n
    i = i + 1
    n = float(input('Digite mais um número da soma: '))
print('A soma dos números dados é {} e foram {} números somados.'.format(int(s),i-1))