from random import randint
from time import sleep
print('O dado que iremos jogar é de 6 lados.\n'
      'E vamos determinar a ordem do proximo jogo!!!!')
n = int(input('Digite o número de jogadores'))
# Determinar os valores que foram jogados
l_jogarores = []
play = {}
i = 1
while i <= n:
    a = str('jogador'+str(i))
    play[a] = randint(1,6)
    print(f'O jogador{i} tirou {play[a]}')
    l_jogarores.append(play.copy())
    play.clear()
    sleep(0.5)
    i += 1

#criar a lista com os números que foram sorteados, e deixalos na ordem
l_num = []
for c in range(0,len(l_jogarores)):
    l_num.append(l_jogarores[c][str('jogador'+str(c+1))])
print('-=' * 15, '\n Deixando em ordem \n','-=' * 15)
sleep(3)

#relacionar os números da tabela acima com os nomes dos jogadores, e para não contar infinitas vezez
#zerar os maiores números
k = 1
l = len(l_jogarores)
while l != 0:
    a = max(l_num)
    for c in range(0,len((l_jogarores))):
        if a == l_jogarores[c][str('jogador'+str(c+1))]:
            print(f'O {k}º jogador é o {str("jogador"+str(c+1))}')
            l_num[l_num.index(a)] = 0
            sleep(0.5)
            k += 1
            l -= 1

print('-----BOM JOGO-----')