from cores import *
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print(f'{cores["azul"]}Analisando os números...{limpar}')
if n1>n2:
    print(f'O primeiro valor é {cores["verde"]}maior{limpar}')
elif n2==n1:
    print(f'Não existe valor maior, os dois são {cores["roxo"]}iguais{limpar}!')
else:
    print(f'O segundo valor é {cores["verde"]}maior{limpar}')
