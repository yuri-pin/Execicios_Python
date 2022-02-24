num = int(input('Digite um número que se quer saber o seu fatorial: '))
i = 1
fat = 1
while i <= num:
    fat = i*fat
    i = i + 1
print(fat)