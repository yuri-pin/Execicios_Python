geral = []
while True:
    pessoa = {}
    pessoa['nome'] = input('Digite o nome da pessoa: ').strip().capitalize()
    pessoa['sexo'] = input('Digite o sexo da pessoa (M/F): ').strip()[0]
    while pessoa['sexo'] not in 'MmFf':
        print('Erro! \n'
              'Digite novamente')
        pessoa['sexo'] = input('Digite o sexo da pessoa (M/F): ').strip()[0]
    pessoa['idade'] = int(input('Digite a idade a idade da pessoa: '))
    geral.append(pessoa.copy())
    pessoa.clear()
    r = input('Deseja continuar(S/N)? ').strip()[0]
    while r not in 'SsNn':
        print('Erro! \n'
              'Digite novamente')
        r = input('Deseja continuar(S/N)? ')
    if r in 'Nn':
        break
tot_idade = 0
for c in range(0, len(geral)):
    tot_idade += geral[c]["idade"]

print(f'A) Ao todo foram {len(geral)} pessoas cadastradas.')
print(f'B) A média das idades é de {tot_idade/len(geral)}')
print(f'C) A lista das mulheres é: ')
for c in range(0, len(geral)):
    if geral[c]['sexo'] in 'Ff':
        print(geral[c]['nome'])
print(f'D) A lista das pessoas com idade acima da média é: ')
for c in range(0, len(geral)):
    if geral[c]['idade'] > tot_idade/len(geral):
        print(geral[c]['nome'])