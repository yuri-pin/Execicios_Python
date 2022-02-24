lista = list()
b = True
while b:
    a = int(input('Digite um número: '))
    if int(len(lista)) == 0:
        lista.append(a)
    if a < lista[0]:
        lista.insert(0,a)
    if a > lista[int(len(lista))-1]:
        lista.append(a)
    for c in range(1,len(lista)):
        if lista[c-1] < a < lista[c] and c < int(len(lista)):
            lista.insert(c, a)
    r = input('pretende continuar (S/N)').strip().upper()[0]
    while r != 'S' and r != 'N':
        print('valor digitado com erro. Digite novamente.')
        r = input('pretende continuar (S/N)').strip().upper()[0]
    if r == 'N':
        b = False
print('A sequência que foi digitada é {}'.format(lista))


