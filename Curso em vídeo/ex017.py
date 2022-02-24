from math import sqrt
c1 = float(input('Digite o valor de um cateto : '))
c2 = float(input('digite o valor do outro cateto : '))
#h = ((c1)**2 + (c2)**2)**(1/2)
h = sqrt((c1)**2 + (c2)**2)
print(h)