from random import randint
from time import sleep

principal = []
n = int(input('Digite quantos jogos se deseja: '))
for k in range(0,n):
    lista = list()
    c = 1
    while c < 7:
        a = randint(1, 60)
        if a not in lista:
            lista.append(a)
            c += 1
    lista.sort()
    principal.append(lista[:])
    lista.clear()
    print(f'{k+1:>2}ª Jogo é {principal[k]}')
    sleep(0.3)

