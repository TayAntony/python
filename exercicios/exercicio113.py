from cores import *
def leiaInt(txt):
    while True:
        try:    
            n = int(input(txt))
        except (ValueError, TypeError):
            print(f'{cores["vermelho"]}ERRO! Digite um número inteiro válido.{limpar}')
            continue
        except (KeyboardInterrupt):
            print(f'{cores["vermelho"]}O usuário preferiu não digitar.{limpar}')
            return 0
        else:
            return n

def leiaReal(txt=0):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print(f'{cores["vermelho"]}ERRO! Digite um número real válido.{limpar}')
            continue
        except (KeyboardInterrupt):
            print(f'{cores["vermelho"]}O usuário preferiu não digitar.{limpar}')
            return 0
        else:
            return n


i = leiaInt('Digite um número INTEIRO: ')
r = leiaReal('Digite um número REAL: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}!')
