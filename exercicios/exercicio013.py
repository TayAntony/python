salário = int(input('Qual o valor do salário? '))
aumento = float(salário*0.15)
total = (salário + aumento)
print(f'O total do novo salário após 15% de aumento é de: R${total:.2f}!')