from datetime import datetime
ano = datetime.now().year
dados = {}
dados['nome'] = input('Digite seu nome: ')
nas = int(input('Digite o ano de nascimento: '))
dados['idade'] = ano - nas
dados['CTPS'] = int(input('digite o número da sua carteira de trabalho: '))
if dados['CTPS'] == 0:
    dados['fim_con'] = '35 anos após o início da contribuição'
    dados['salario'] = 'sem salário'
else:
    ini_con = int(input('Digite o ano de inicio da contribuição'))
    dados['fim_con'] = 35-(ano - ini_con) + ano - nas
    dados['salario'] = float(input('Digite quanto se recebe de salário'))
print(dados)
