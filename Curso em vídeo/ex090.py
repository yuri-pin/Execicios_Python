test = {}
test['Nome'] = input('Digite o nome do aluno: ')
test['Media'] = float(input('Digite a média: '))
if test['Media'] < 6:
    test['Situação'] = 'Reprovado'
else:
    test['Situação'] = 'Aprovado'

print(test)