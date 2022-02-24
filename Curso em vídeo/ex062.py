a0 = float(input('Digite o primeiro termo da progressão aritmetica: '))
r = float(input('Digite a razão da progressão aritmetica: '))
n = int(input('Digite quantos termos se quer da sequencia'))
i = 0
while i < n:
    print('a{} = {}'.format(i, a0 + (i)*r))
    i += 1