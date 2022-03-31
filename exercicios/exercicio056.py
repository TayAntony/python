tot = 0
media = 0
mih = 0
homem = 0
mulher = 0
for p in range(1,5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    tot += idade
    if p == 1 and sexo in 'Mm':
        mih = idade
        homem = nome
    if sexo in 'Mm' and idade > mih:
        mih = idade
        homem = nome
    if sexo in 'Ff' and idade <20:
        mulher += 1
media = tot/4
print(f'A média de idade do grupo é de: {media:.2f} anos!')
print(f'O homem mais velho tem {mih} anos e se chama {homem}.')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos.')
