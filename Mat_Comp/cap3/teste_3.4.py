from numpy import loadtxt
from pylab import plot, show

def formatar_dados(arq):
    a = open(arq, 'rt')
    lista = a.readlines()
    for i in range(0,len(lista)):
        lista[i] = lista[i].replace(',', '.')
    return lista

#loadtxt carrega os dados de um arquivo de texto
#Útil para plotar dados obtidos em experimentos e float é o tipo de dados retirados.

data = loadtxt(formatar_dados('teste_3.4.txt'), float)
# data[:,i] são todos os dados devido ao ':' e da coluna i
plot(data[:,0],data[:,1])
show()
