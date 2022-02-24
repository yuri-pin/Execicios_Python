from random import randint
a = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
maior = 0
menor = 20
for c in range(0, 5):
    if a[c] >= maior:
        maior = a[c]
    elif a[c] <= menor:
        menor = a[c]
print(f'A tupla é {a}\n'
      f'O maior termo é {maior}\n'
      f'O menor termo é {menor}')

# para encontrar valores maximos e mínimos em tuplas apenas usar max(tupla) e min(tupla)