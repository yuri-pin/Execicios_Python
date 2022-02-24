n = int(input('Digite quantos termos se quer na sequência de Fibonacci: '))
if n == 1:
    print(1)
if n == 2:
    print(1)
    print(1)
if n > 2:
    a1 = 1
    a2 = 1
    i = 2
    print('{} \n'
          '{}'. format(a1, a2))
    while i<n:
        a_soma = a1 + a2
        print(a_soma)
        a1 = a2
        a2 = a_soma
        i = i + 1
