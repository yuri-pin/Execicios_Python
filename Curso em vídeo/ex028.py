import random
a = random.randint(0,5)
print('Pensei em um número entre 0 e 5, tente adivinhar.')
b = int(input('Digite um número inteiro entre 0 e 5: '))

if a == b:
    print('Parabéns, você acertou o número que eu pensei ')
else:
    print('Você errou! Mas não desista, vamos tentar outra rodada?')