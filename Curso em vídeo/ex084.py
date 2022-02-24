grupo = []
pessoa = []
b = True
while b:
    nome = pessoa.append(input('Digite o nome da pessoa: '))
    peso = pessoa.append(float(input('Digite o peso da pessoa: ')))
    grupo.append(pessoa[:])
    pessoa.clear()
    rec = str(input('Deseja continuar? (S/N)'))
    while rec not in 'SNsn':
        print('erro na digitação. Tente denovo.')
        rec = str(input('Deseja continuar? (S/N)'))
    if rec in 'Nn':
        b = False
print('O número de pessoas adicionadas foi {}'.format(len(grupo)))

p_M = p_m = 0
for c in range(0, len(grupo)):
    if c == 0:
        p_m = p_M = grupo[c][1]
    else:
        if grupo[c][1] >= p_M:
            p_M = grupo[c][1]
        if grupo[c][1] <= p_m:
            p_m = grupo[c][1]
print(f'O menor peso é {p_m} e das pessoas ', end= '')
for p in grupo:
    if p[1] == p_M:
        print(f'{p[0]}', end=' ')
print(f'\nO maior peso é {p_M} e das pessoas ', end='')
for p in grupo:
    if p[1] == p_m:
        print(f'{p[0]}', end=' ')