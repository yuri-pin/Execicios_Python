a = True
print('Para não aparecer a tabuada digite um número negativo')
while a:
    num = int(input('Digite um numero que se quer saber a tabuada: '))
    if num < 0:
        break
    print('-'*15)
    for n in range(1,11):
        print('{} x {:2} = {}'.format(num, n, num*n))
    print('-' * 15)
    b = input('Deseja saber outra tabuada (S/N)').strip().upper()
    print('-'*15, '\n')
    while b != 'S' and b != 'N':
        print('Informação incorreta')
        b = input('Deseja saber outra tabuada (S/N)').strip().upper()
        print('-' * 15, '\n')
    if b == 'N':
        a = False

print('Acabou')