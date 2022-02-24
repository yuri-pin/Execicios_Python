grupo = [[],[],[]]
n = int(input('Digite quantos números se quer digitar: '))
for c in range(0,n):
    a = int(input(f'Digite o {c+1}ª número'))
    grupo[0].append(a)
    if a%2 == 0:
        grupo[1].append(a)
    else:
        grupo[2].append(a)
grupo[1].sort()
print('A lista com o os números pares é {}'.format(grupo[1]))
grupo[2].sort()
print('A lista com o os números ímpares é {}'.format(grupo[2]))
