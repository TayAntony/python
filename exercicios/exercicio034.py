from cores import *
salario = float(input('Digite o salário do funcionário? R$'))
salario1 = (salario*0.1) + salario
salario2 = (salario*0.15) + salario
if salario >= 1250:
    print(f'Seu aumento é de {cores["vermelho"]}R${salario:.2f}{limpar} para {cores["verde"]}R${salario1:.2f}{limpar}!')
else:
    print(f'Seu aumento é de {cores["vermelho"]}R${salario:.2f}{limpar} para {cores["verde"]}R${salario2:.2f}{limpar}!')