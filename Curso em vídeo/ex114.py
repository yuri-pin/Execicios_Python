import urllib
import urllib.request
a = input('Digite a URL do site desejado: ')
try:
    site = urllib.request.urlopen(a)
except:
    print('não site não está disponível')
else:
    print('Consegui acessar o site')