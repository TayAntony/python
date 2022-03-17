nome = str(input('Digite seu nome completo: ')).strip()
tamanho = len(nome.replace(' ','')) #ou usar - nome.count(' ') para tirar todos os espaços
snome = len(nome.split()[0])
pnome = nome.split()[0]
print('Analisando seu nome...')
print(f'Seu nome maiúsculo é: {nome.upper()}')
print(f'Seu nome minúsculo é: {nome.lower()}')
print(f'Seu nome tem um total de {tamanho} letras.')
print(f'Seu primeiro nome é {pnome} e tem {snome} letras.')