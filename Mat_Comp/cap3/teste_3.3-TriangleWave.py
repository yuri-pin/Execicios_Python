from pylab import plot, show
from numpy import linspace, sin

#linspace(a,b,c) tem inicio no ponto 'a' fim no ponto 'b' e é dividido em 'c' partes
x = linspace(-10, 10, 1000)
f = 0
for i in range(0, 100):
    f = f + (-1)**i*sin((2*i+1)*x)/((2*i+1)**2)
y = f
plot(x, y)
show()