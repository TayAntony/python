jogadores = []
dados = {}
partidas = []
while True:
    dados.clear()
    dados['Jogador'] = input('Nome do Jogador: ').upper()
    pt = int(input(f'Quantas partidas {dados["Jogador"]} jogou? '))
    partidas.clear()
    for i in range(0, pt):
        partidas.append(int(input(f'  >>>>> Quantos gols na {i+1}ª partida? ')))
    dados['Gols'] = partidas[:]
    dados['Total'] = sum(dados['Gols'])
    jogadores.append(dados.copy())
    while True:
        continuar = input('Deseja continuar? [S/N]: ').upper()[0].strip()
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas S ou N...')
    if continuar == 'N':
        break

print('-'*40)
print('Nº ', end='')
for i in dados.keys():
    print(f'{i:<17}', end='')
print()
print('-'*40)
for k, v in enumerate(jogadores):
    print (f'{k:<2} ', end='')
    for d in v.values():
        print(f'{str(d):<17}', end='')
    print()
print('-='*20)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 encerra) '))
    if busca == 999:
        print('<< VOLTE SEMPRE >>')
        break
    if busca >= len(jogadores):
        print(f'Não existe jogador com código {busca}')
    else:
        print(f'Levantamento do jogador {jogadores[busca]["Jogador"]}:')
        for i, g in enumerate (jogadores[busca]["Gols"]):
            print(f'      No {i+1}º jogo fez {g} gols.')
    print('='*40)
