salario = float(input('Digite o salário do funcionário? R$'))
salario1 = (salario*0.1) + salario
salario2 = (salario*0.15) + salario
if salario >= 1250:
    print(f'Seu aumento é de R${salario:.2f} para R${salario1:.2f}!')
else:
    print(f'Seu aumento é de R${salario:.2f} para R${salario2:.2f}!')