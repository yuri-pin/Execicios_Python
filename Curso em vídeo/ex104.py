def leiaInt(obj):
    while True:
        k = str(input(obj)).strip()
        if k.isnumeric():
            return True
            break
        else:
            print('\033[31mErro! o valor digitado não é um número.\033[m')


a = leiaInt('Digite um número: ')
print(a)

