#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
#mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
def sortear(n):
    lista = []
    for k in range(0, n):
        lista.append(randint(-10, 10))
    return lista

def soma_par(list):
    s = 0
    k = len(list)
    for i in range(0, k):
        if list[i]%2 == 0:
            s = s + list[i]
    return s

a = sortear(5)
print(a)
print(soma_par(a))