l1 = float(input('Digite o comprimento do primeiro lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))

if l1>abs(l2-l3) and l2>abs(l1-l3) and l3>abs(l1-l3) and l1<(l2+l3) and l2<l1+l3 and l3<l1+l2:
    print('Os lados dados podem formar um triangulo')
else:
    print('Os lados dados não podem formar um triangulo')