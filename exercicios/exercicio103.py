def dados(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato!')


jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    dados(gol=gols)
else:
    dados(jogador, gols)
