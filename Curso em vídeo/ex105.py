def notas(*n, sit=False):
    """

    :param n: Sequência de notas .
                Sequence of grades
    :param sit: Parametro que irá determinar a situação média da classe.
                Parameter that will determine the situation of the class.
    :return: Retorna um dicionário com a quantidade de notas digitadas, a maior, a menor e a média das notas. E caso
     sit = True, descrever a situação da classe, sendo média maior que 7 a situação é boa, se está entre 5 e 7 é regular
     e se menor que 5 é ruim.
    """
    turma = {}
    turma['quant'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    s = 0
    for k in range(0,len(n)):
        s += n[k]
    turma['média'] =s/len(n)
    if not sit:
        if s/len(n) < 5 :
            turma['situação'] = 'RUIM'
        elif s/len(n) < 6:
            turma['situação'] = 'REGULAR'
        else:
            turma['situação'] = 'BOA'
    return turma


print(notas(5.5, 6.5, 9.5, sit=True))
print('-='*30)
print(notas(5.5,6.5,9.5))
