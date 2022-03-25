from cores import *
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestaçao = casa / (anos*12)
min = salario*0.3
print(f'Para financiar uma casa de R${casa:.2f} em {anos} anos é preciso ter uma prestação mensal de R${min:.2f}!')
if prestaçao<=min:
    print(f'Seu empréstimo foi {cores["verde"]}ACEITO{limpar}!')
else:
    print(f'Sinto muito, seu salário não é suficiente para pagar a prestação mensal!', end='')
    print(f'{cores["vermelho"]}não será possível fazer o empréstimo{limpar}!')