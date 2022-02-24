from datetime import date
nas = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year

if ano-nas > 18:
    print('O senhor tem {} anos'.format(ano-nas))
    print('Já passou da época de se alistar.')
    a = input('Já se alistou?(Sim ou Não): ').upper()
    if a == 'SIM':
        print('O senhor está regularizado com as forças armadas')
    elif a == 'NÃO':
        print('O senhor precisa se regularizar com as forças armadas, o mais rápido possível.')
    else:
        print('O senhor não respondeu a pergunta. reinicie.')

elif ano-nas < 18:
    print('O senhor ainda tem {} anos.'.format(ano-nas))
    print('Ainda faltam {} anos para se alistar.'.format(18-ano+nas))
    print('O senhor se alistará no ano de {}'.format(18+nas))
else:
    print('Esse ano o senhor tem que se alistar, entre no site do exército e se aliste.')
