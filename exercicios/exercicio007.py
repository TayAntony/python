from cores import *
nota1 = float(input('Qual é a primeira nota? '))
nota2 = float(input('Qual é a segunda nota? '))
total = nota1 + nota2
media = total/2
print(f'A soma das duas notas é {cores["verde"]}{total}{limpar} e a média é {cores["azul"]}{media:.1f}{limpar}!')