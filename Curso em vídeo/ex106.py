from time import sleep
def txt_formatado(txt):
    print('~'*(len(txt)+4))
    print('  '+txt+'  ')
    print('~' * (len(txt) + 4))

def pesquisa(obj):
    while True:
        k = input(obj).strip().lower()
        if k == 'fim':
            print('\033[7;31m',end='')
            txt_formatado('Até logo')
            print('\033[m', end='')
            break
        else:
            print('\033[7;34m', end='')
            txt_formatado(f"Acessando o manual do camando '{k}'")
            print('\033[m', end='')
            print('\033[7m')
            print(help(k))
            print('\033[m', end='')
            print('\033[7;32m', end='')
            txt_formatado('Sistema de ajuda PyHELP')
            print('\033[m',end='')




#Programa principal
pesquisa('Função ou Biblioteca > ')