from cores import *
n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
media = (n1+n2)/2
if media > 7.0:
    print(f'{cores["verde"]}APROVADO{limpar}')
elif media >= 5 and media <=6.9:
    print(f'{cores["amarelo"]}RECUPERAÇÃO{limpar}')
elif media <5:
    print(f'{cores["vermelho"]}REPROVADO{limpar}')

