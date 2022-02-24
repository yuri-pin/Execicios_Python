jogador = {}
jogador['nome'] = input('Digite o nome do jogador: ')
jogador['partidas'] = int(input('quantas partidas ele jogou: '))
gols = []
tot_gol = 0
for i in range (0,jogador['partidas']):
    g = int(input(f'Digite quantos gols foram feitos na {i+1}ª partida: '))
    gols.append(g)
    tot_gol += g
jogador['gol'] = gols
jogador['total'] = tot_gol
print('-='*30, '\n',jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
