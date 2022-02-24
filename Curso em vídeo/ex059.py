a1 = int(input('Digite um valor inteiro: '))
a2 = int(input('Digite um valor inteiro: '))
n = 1
print('---'*7)
print('[1] Somar \n'
      '[2] Multiplicar \n'
      '[3] Maior \n'
      '[4] Novos Números \n'
      '[5] Sair')
print('---'*7)
while n != 5 and n < 6:
      n = int(input('Digite o comando que se quer tomar com os números dados: '))
      if n == 1:
            print('A soma do a1 e de a2 é igual a {}'.format(a1+a2))
      if n == 2:
            print('O produto de a1 e a2 é igual a {}'.format(a1*a2))
      if n == 3:
            if a1 > a2:
                  print('O maior dos números é {}'.format(a1))
            elif a1 < a2:
                  print('O maior dos números é {}'.format(a2))
            else:
                  print('Os números são iguais')
      if n == 4:
            a1 = int(input('Digite um valor inteiro: '))
            a2 = int(input('Digite um valor inteiro: '))
print('Terminou')
