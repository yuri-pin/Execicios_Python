ano = int(input('Digite o ano que se quer saber se é bissexto ou não: '))
if ano%4 == 0:
    print('{} é bissexto!'.format(ano))
else:
    print('{} não é bissexto!'.format(ano))