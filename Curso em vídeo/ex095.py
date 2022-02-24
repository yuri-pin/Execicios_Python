time = []
while True:
    jogador = {}
    jogador['nome'] = input('Digite o nome do jogador: ').strip().capitalize()
    jogador['partidas'] = int(input('quantas partidas ele jogou: '))
    gols = []
    tot_gol = 0
    for i in range (0,jogador['partidas']):
        g = int(input(f'Digite quantos gols foram feitos na {i+1}ª partida: '))
        gols.append(g)
        tot_gol += g
    jogador['gol'] = gols
    jogador['total'] = tot_gol
    time.append(jogador.copy())
    jogador.clear()
    r = input('Deseja continuar(S/N)? ').strip()[0]
    while r not in 'SsNn':
        print('Erro! \n'
              'Digite novamente')
        r = input('Deseja continuar(S/N)? ')
    if r in 'Nn':
        break
print('-='*30)
for c in range(0, len(time)):
    print(f'{c:<2}', f'{time[c]["nome"]:<15}', f'{time[c]["partidas"]:>4}', f'{time[c]["total"]:>4}')
print('-='*30)