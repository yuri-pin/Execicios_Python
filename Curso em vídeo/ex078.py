a = [int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite o último número: '))]
print(f'O menor valor de {a} é {min(a)} e se encontra na posição ', end='')
for c, v in enumerate(a):
     if v == min(a):
          print(c+1, end=' ')
print(f'\nO maior valor de {a} é {max(a)} e se encontra na posição ', end='')
for c , v in enumerate(a):
     if v == max(a):
          print(c+1, end=' ')
