dis = float(input('Digite a distancia a ser percorrida em Km: '))
if dis <= 200:
    print('o valor a ser pago é de R${}'.format(dis*0.50))
else:
    print('o valor a ser pago é de R${}'.format(dis*0.45))