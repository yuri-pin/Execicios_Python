vel = float(input('Digite qual a velocidade do carro: '))
if vel<=80:
    print('esse carro não ultrapassou o limite de velocidade')
else:
    print('esse carro será multado e a multa referente será de R${:.2f}'.format((vel-80)*7))