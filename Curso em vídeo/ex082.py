l_1 = []
b = True
while b:
    l_1.append(int(input('Digite um número: ')))
    a = input('Deseja continuar? (S/N)').strip()[0]
    if a in 'Nn':
        b = False
    while a not in 'SNsn':
        a = input('Deseja continuar? (S/N)')
l_p = []
l_i = []
for c in range(0,int(len(l_1))):
    if l_1[c] % 2 == 0:
        l_p.append(l_1[c])
    elif l_1[c] % 2 == 1:
        l_i.append(l_1[c])

print('A lista dos termos pares é, ',l_p)
print('A lista dos termos ímpares é, ',l_i)
