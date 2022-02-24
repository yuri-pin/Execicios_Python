número = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze','dezesseis', 'dezessete', 'dezoito', 'dezenove','vinte')
num = int(input('Digite um número entre 0 e 20: '))
while num > 20 or num < 0:
    print('\33[31mNúmero não está correto. \n'
          'Digite novamente.\33[m')
    num = int(input('Digite um número entre 0 e 20: '))
print(f'o número que você escolheu é {número[num]}')