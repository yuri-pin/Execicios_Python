from numpy import linspace, sin, cos
from pylab import plot, show
from math import pi, e

#deltóide curvo
t = linspace(0,2*pi,100)
x = 2*cos(t)+cos(2*t)
y = 2*sin(t)-sin(2*t)
plot(x,y)
show()


#espiral
k = linspace(0,10*pi,1000)
x = (k**2)*cos(k)
y = (k**2)*sin(k)
plot(x, y)
show()


#Butterfly
l = linspace(0,10*pi,1000)
r = e**cos(l) - 2*cos(4*l) + (sin(l/12))**5
x = r*cos(l)
y = r*sin(l)
plot(x, y)
show()

