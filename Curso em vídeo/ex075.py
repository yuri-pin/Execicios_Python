a = (int(input('Digite o primeiro número:')), int(input('Digite mais um número:')),
     int(input('Digite mais um número:')), int(input('Digite o último número:')))
print('-='*15)
print(f'Você digitou os números {a}')
print(f'O número 9 apareceu {a.count(9)} vezes')
if 3 in a:
     print(f'O número 3 tem sua primeira aparição na posição {a.index(3) + 1}')
else:
     print('O 3 não aparece nessa sequência')
cont_p = 0
for c in range(0, 4):
     if a[c]%2 == 0:
          cont_p += 1
print(f'O númertos pares aparecem {cont_p} vezes')
print('-='*15)