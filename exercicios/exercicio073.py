colocacao = ('São Paulo','Coritiba','Corinthians','Atlétigo-MG','Ceará','Avaí','Cuiabá','Bragantino','Juventude','Flamengo','Atlético-GO','Santos','Fluminense','Palmeiras','Fortaleza','América-MG','Botafogo','Internacional',
'Goiás','Athletico-PR')
print('=-'*20)
print(f'Lista de times do Brasileirão 2022: {colocacao}')
print('=-'*20)
print(f'Os 5 primeiros são: {colocacao[0:5]}')
print('=-'*20)
print(f'Os 4 últimos são: {colocacao[16:]}')
print('=-'*20)
print(f'Times em ordem alfabética: {sorted(colocacao)}')
print('=-'*20)
print(f'O Flamengo está na {colocacao.index("Flamengo")+1}ª posição')
print('=-'*20)
