a = True
while a:
    nome_produto = input('Digite o nome do produto: ')
    preco_produto = int(input('Digite o preço dos produtos: '))
    nome_barato = ' '
    preco_barato = preco_produto
    if preco_barato <= preco_produto:
        nome_barato = nome_produto
        preco_barato = preco_produto
    r = input('deseja continuar? [S/N]: ').strip().upper()
    while r!='S' and r !='N':
        print('Houve um erro de digitação.\n'
              'Tente novamente\n')
        r = input('deseja continuar? [S/N]').strip().upper()
    if r == 'N':
        break

print(f'O produto mais barato é o {nome_barato} e seu preço é {preco_barato}')