print('='*5, 'CADASTROS' ,'='*5)
cont = maior_idade = homens = mulher = 0
while True:
    idade = int(input('Idade: '))
    if idade >=18:
        maior_idade += 1
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade >20:
        mulher += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('-'*20)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        print('Estatísticas:')
        break
print(f'O total de pessoas com mais de 18 anos é: {maior_idade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulher} mulher(es) com menos de 20 anos')
