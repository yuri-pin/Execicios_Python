sex = input('Digite o seu sexo (M/F): ').upper().strip()
while sex != 'M' and sex != 'F':
    print('Você não digitou o que foi pedido, por favor responda novamente.')
    sex = str(input('Digite o seu sexo (M/F): ')).upper().strip()
print('Agradecemos pela resposta!')
