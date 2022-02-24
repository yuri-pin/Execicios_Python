a0 = float(input('Digite o primeiro termo da progressão aritmetica: '))
r = float(input('Digite a razão da progressão aritmetica: '))
i = 0
while i < 10:
    print('a{} = {}'.format(i, a0 + (i)*r))
    i += 1