pc = float(input('Digite o valor da casa que se quer comprar: '))#pp equivale a preço casa
s = float(input('Digite o valor de seu salário: '))# s equivale a salário
p = int(input('Digite em quantos anos se pretende pagar: '))# p equivale ao número de parcelas

pp = pc/(12*p)# pp equivale ao preço da parcela

if pp/s > 0.3:
    print('O empréstimo não será aceito')
else:
    print('O emprestimo será aceito')