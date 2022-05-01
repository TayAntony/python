from time import sleep
dados = {}
pessoas = []
mulheres = []
while True:
    dados['nome'] = input('Nome: ')
    dados['sexo'] = input('Sexo: [M/F] ').upper().strip()
    if dados['sexo'] not in 'FM':
        print('Por favor responda apenas [M ou F]!')
        continue
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    dados.clear()
    continuar = input('Quer continuar? [S/N] ').upper().strip()
    if continuar not in 'SN':
        print('Por favor digite apenas [S ou N]!')
        continue
    elif continuar in 'N':
        break

cont = 0
for pessoa in pessoas:
    cont += pessoa['idade']

media = cont/len(pessoas)

sleep(1)
print('Analisando...')
sleep(1)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
sleep(1)
print(f'B) As mulheres cadastradas foram: ', end='')
for mulher in mulheres:
    print(f'{mulher}... ', end='')
sleep(1)
print(f'\nC) A média de idade é de {media:.2f} anos')
sleep(1)
print(f'D) Lista das pessoas acima da média: ')
for pessoa in pessoas:
    if pessoa['idade'] > media:
        print(f'nome = {pessoa["nome"]}; sexo = {pessoa["sexo"]}; idade = {pessoa["idade"]}')
sleep(1)
print('<< ENCERRADO >>')
