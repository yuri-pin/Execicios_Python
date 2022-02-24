import random
comp = random.randint(0,10)
num = int(input('Digite um número entre 0 e 10: '))
i = 1
while comp != num:
    print('Você errou, tente novamente.')
    num = int(input('Digite um número entre 0 e 10: '))
    i += 1
print('\033[031mVocê acertou!!!! \n'
      'Parabéns \n'
      'Voce usou {} tentativas para acertar\033[031m'.format(i))
