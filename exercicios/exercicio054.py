from datetime import date
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input(f'Digite o ano de nascimento da {pess}ª pessoa: '))
    atual = date.today().year
    idade = atual-nasc
    if idade<18:
        totmenor += 1
    elif idade>=18:
        totmaior += 1
print(f'Ao todo tivemos {totmenor} pessoas menores de idade!')
print(f'E também tivemos {totmaior} pessoas maiores de idade!')
