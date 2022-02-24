np = int(input('Digite o número de pessoas  que se deseja analisar: '))
s = 0
menor_20 = 0
idade_velho = 0
nome_velho = ''
for c in range(1, np+1):
    print('------{}ªPessoa-------'.format(c))
    nome = input('Digite o nome da pessoa:').strip()
    idade = int(input('Digite a idade da pessoa: '))
    sex = input('Digite o sexo da pessoa (M/F): ').upper().strip()
    s = s + idade
    if c == 1 and sex == 'M':
        idade_velho = idade
        nome_velho = nome
    if c != 1 and sex == 'M' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
    if sex == 'F':
        if idade < 20:
            menor_20 = menor_20 + 1
print('-'*20)
média = s/np
print('A media de idade desse grupo é {}'.format(média))
print('O homem mais velho é {} e ele tem {} anos'.format(nome_velho, idade_velho))
print('o número de mulheres menores de 20 anos é {}'.format(menor_20))