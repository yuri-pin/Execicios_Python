import math

num = int(input('Digite um número inteiro que se quer saber se é primo ou não: '))
from math import floor
k = 0
for n in range(2, math.floor(num**(1/2))+1):
    if num%n == 0:
        k = 1
        break
if k == 0:
    print('{} é um numero primo'.format(num))
elif k == 1:
    print('{} não é um número primo'.format(num))