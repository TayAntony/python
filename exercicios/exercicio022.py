from cores import *
nome = str(input('Digite seu nome completo: ')).strip()
tamanho = len(nome.replace(' ','')) #ou usar - nome.count(' ') para tirar todos os espaços
snome = len(nome.split()[0])
pnome = nome.split()[0]
print(f'{cores["preto"]}{bg["branco"]}{fx["negrito"]}Analisando seu nome...{limpar}')
print(f'Seu nome maiúsculo é: {cores["roxo"]}{nome.upper()}{limpar}')
print(f'Seu nome minúsculo é: {cores["vermelho"]}{nome.lower()}{limpar}')
print(f'Seu nome tem um total de {cores["azul"]}{tamanho} letras{limpar}.')
print(f'Seu primeiro nome é {pnome} e tem {snome} letras.')