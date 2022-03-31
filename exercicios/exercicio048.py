soma = 0
cont = 0
for imp in range(1,501,2):
    if imp % 3 == 0:
        cont += 1
        soma += imp
print(f'A soma de todos os {cont} valores é {soma}')