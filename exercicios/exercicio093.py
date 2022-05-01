informacoes = {}
informacoes['Jogador'] = input('Nome do Jogador: ')
qntp = int(input(f'Quantas partidas {informacoes["Jogador"]} jogou? '))
informacoes['Gols'] = []
for i in range (qntp):
    informacoes['Gols'].append(int(input(f'   Quantos gols na {i+1}ª partida? ')))
informacoes['Total'] = sum(informacoes['Gols'])
print('-'*30)
print(informacoes)
print('-'*30)
for k, v in informacoes.items():
    print(f'O campo {k} tem o valor {v}.')
print('-'*30)
print(f'O jogador {informacoes["Jogador"]} jogou {qntp} partidas!')
for i in range (qntp):
    print(f'    => Na partida {i+1}, fez {informacoes["Gols"][i]} gols.')
print(f'Foi um total de {informacoes["Total"]} gols')


































