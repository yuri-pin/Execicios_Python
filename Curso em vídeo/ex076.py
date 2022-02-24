a = ('Pao', 2.00, 'Batata', 5.00)
if len(a)%2 != 0:
    print('sua lista de preços contem algum erro!')
for c in range(0, int(len(a)/2)):
    print(f'{a[2*c]:.<30}R${a[2*c+1]:>7.2f}')