from numpy import empty
from pylab import imshow, gray, show,xlabel,ylabel
from math import pi


# Definindo as constantes físicas
epsilon = 8.85*(10**(-12))
k = 1/(4*pi*epsilon)
# potencial de uma carga -> = k*q/r

# Definindo o formato do print
xlabel('x - axis')
ylabel('y - axis')
lado = 0.5
pontos = 500
espaços = lado/pontos

# Definindo posições das cargas
print('O valor absoluto das cargas é 1.2')
q1 = 10**-12
x1 = 0.4
y1 = 0.3

q2 = -10**-12
x2 = 0.2
y2 = 0.1

#Definindo a impressão
mapa = empty([pontos, pontos], float)
for j in range(pontos):
    y = j*espaços
    for i in range(pontos):
        x = i*espaços
        r1 = ((x-x1)**2 + (y-y1)**2)**1/2
        r2 = ((x-x2)**2 + (y-y2)**2)**1/2
        if r1 != 0 and r2 != 0:
            v = k*(q1/r1 + q2/r2)
        elif r1 == 0:
            v = k*q2/r2
        elif r2 == 0:
            v = k*q1/r1
        if abs(v) < 10:
            mapa[i, j] = v
        elif v < 0:
            mapa[i, j] = -10
        elif v > 0:
            mapa[i, j] = 10


imshow(mapa, origin="lower", extent=[0, lado, 0, lado])
gray()
show()
