s =0
k = int(input('Digite quantos números se quer digitar: '))
for n in range(1,k+1):
    b = int(input('Digite um número inteiro: '))
    if b%2 == 0:
        s = s + b
print('A soma dos número pares é {} entre os {} números informados.'.format(s,k))