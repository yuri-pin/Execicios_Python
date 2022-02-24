a0 = float(input('Digite o valor do primeiro termo (a0) da progressão aritmética: '))
r = float(input('Digite a razão da progressão aritmética: '))
for n in range(1,11):
    an = a0 + n*r
    print('O valor de a{} é {}'.format(n,an))