l1 = float(input('Digite o comprimento do primeiro lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))
# tome l1 como o maior
maior = l1
if l2 > l3 and l2 > l1:
    maior = l2
if l3 > l2 and l3 > l1:
    maior = l3
# tome l1 como o menor
menor = l1
if l2 < l3 and l2 < l1:
    menor = l2
if l3 < l2 and l3 < l1:
    menor = l3

print(maior)
print(menor)