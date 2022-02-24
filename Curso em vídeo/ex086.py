mat = []
n = int(input('Digite a dimensão da matriz: '))
for c in range(0,n):
    linha = []
    for b in range(0, n):
        termo = int(input(f'Digite o valor a{c,b}'))
        linha.append(termo)
    mat.append(linha[:])
    linha.clear()
for k in range(0,n):
    for b in range(0, n):
        print(f'{mat[k][b]:>4}', end='')
    print()
