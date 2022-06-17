from cores import *
def leiaInt(txt):
    try:    
        n = int(input(txt))
        return n
    except ValueError:
        print(f'{cores["vermelho"]}ERRO! Digite um número inteiro válido.{limpar}')
        return leiaInt(txt)


def leiaReal(txt):
    try:
        n = float(input(txt))
        return n
    except ValueError:
        print(f'{cores["vermelho"]}ERRO! Digite um número real válido.{limpar}')
        return leiaReal(txt)

i = leiaInt('Digite um número INTEIRO: ')
r = leiaReal('Digite um número REAL: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}!')
