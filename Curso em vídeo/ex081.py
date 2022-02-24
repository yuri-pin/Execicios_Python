l_1 = []
b = True
cont = 0
while b:
    l_1.append(int(input('Digite um núemro: ')))
    cont += 1
    r = input('pretende continuar (S/N)').strip().upper()[0]
    while r != 'S' and r != 'N':
        print('valor digitado com erro. Digite novamente.')
        r = input('pretende continuar (S/N)').strip().upper()[0]
    if r == 'N':
        b = False
print('A quantidade de números digitados foi {}'.format(cont))
l_1.sort(reverse = True)
print(f'A lista l_1 escrita de forma decrescente fica {l_1}')
if 5 in l_1:
    print(f'O 5 está na lista na posição ', end = '')
    for c, v in enumerate(l_1):
        if v == 5:
            print(c+1, end=' ')
else:
    print('O elemente 5 não pertence à lista.')