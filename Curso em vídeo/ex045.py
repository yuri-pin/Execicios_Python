import random
from time import sleep

lista = ['pedra','papel', 'tesoura']
comp = random.choice(lista)
print('Para escolher entre pedra, papel ou tesoura digite.')
print('-=-' * 12)
print('[ 0 ] = pedra \n'
      '[ 1 ] = papel \n'
      '[ 2 ] = tesoura')
print('-=-' * 12)
p = int(input('escolha uma das opções para jogar: '))
print('J0')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
if p == 0:
    if comp == 'papel':
        print('O computador ganhou, tente novamente.')
    elif comp == 'pedra':
        print('Empate, tente novamente.')
    else:
        print('Parabens você ganhou!!!!')
elif p == 1:
    if comp == 'papel':
        print('Empate, tente novamente.')
    elif comp == 'pedra':
        print('Parabens você ganhou!!!!')
    else:
        print('O computador ganhou, tente novamente.')
elif p == 2:
    if comp == 'papel':
        print('Parabens você ganhou!!!!')
    elif comp == 'pedra':
        print('O computador ganhou, tente novamente.')
    else:
        print('Empate, tente novamente.')

print('o computador pensou em jogar {}'.format(comp))