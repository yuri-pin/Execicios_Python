mat = []
n = int(input('Digite a dimensão da matriz: '))
for c in range(0,n):
    linha = []
    for b in range(0, n):
        termo = int(input(f'Digite o valor a{c,b}'))
        linha.append(termo)
    mat.append(linha[:])
    linha.clear()
print('-='*30)
for k in range(0,n):
    for b in range(0, n):
        print(f'{mat[k][b]:>4}', end='')
    print()
print('-='*30)
print('O que se quer saber da matriz? \n'
      '[0] - soma de todos os termos \n'
      '[1] - soma de uma linha \n'
      '[2] - soma de uma coluna \n'
      '[3] - traço')
a = int(input('Digite um dos valores mostrados:'))
if a == 0:
    s = 0
    for k in range(0, n):
        for b in range(0, n):
            s = s + mat[k][b]
    print('A soma dos termos é igual a {}'.format(s))
if a == 1:
    l = int(input(f'Digite a linha de que se quer saber a soma (entre 0 e {n-1}): '))
    s = 0
    for b in range(0, n):
        s = s + mat[l][b]
    print(f'A soma dos termos da linha {l} é igual a {s}')
if a == 2:
    l = int(input(f'Digite a coluna de que se quer saber a soma (entre 0 e {n-1}): '))
    s = 0
    for b in range(0, n):
        s = s + mat[b][l]
    print(f'A soma dos termos da linha {l} é igual a {s}')
if a == 3:
    s = 0
    for b in range(0, n):
        s = s + mat[b][b]
    print(f'O traço vale {s}')