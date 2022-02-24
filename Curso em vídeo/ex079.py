a = list()
b = True
d = True
while b:
    a.append(int(input('Digite um valor: ')))
    for c in range(0,len(a)-1):
        if a[c] == a[int(len(a))-1]:
            d = False
            a.pop()
    if not d:
        print('Valoe duplicado. Não irei adicionar...')
    print('Adicionado com sucesso...')
    r = input('pretende continuar (S/N)').strip().upper()[0]
    while r != 'S' and r != 'N':
        print('valor digitado com erro. Digite novamente.')
        r = input('pretende continuar (S/N)').strip().upper()[0]
    if r == 'N':
        b = False
print('A sequência que foi digitada é {}'.format(sorted(a)))

