dias = int(input('Por quantos dias o carro foi alugado? '))
km = int(input('Quantos quilomêtros foram rodados? '))
total = float(dias*60.00) + (km*0.15)
print(f'O total a pagar é de R${total:.2f}')