num = int(input('Digite um numero que se quer saber a tabuada: '))
print('-'*15)
for n in range(1,11):
    print('{} x {:2} = {}'.format(num, n, num*n))
print('-' * 15)
