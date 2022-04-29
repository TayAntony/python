from datetime import datetime
from time import sleep
dados = {}
dados['Nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 = não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + (dados['Contratação'] + 35 - datetime.now().year)
print('-'*30)
for k, v in dados.items():
    print(f'  -- {k} tem o valor {v}')
    sleep(1)
