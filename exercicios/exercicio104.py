from cores import *
def leiaInt(txt):
    """
    -> O código lê um número n com a função leiaInt
    o try cria o input de n no formato de txt (texto) e retorna o valor de n
    o except printa um erro se o valor digitado no input try for diferente de um número e retorna a função leiaInt
    """
    try:    
        n = int(input(txt))
        return n
    except ValueError:
        print(f'{cores["vermelho"]}ERRO! Digite um número válido.{limpar}')
        return leiaInt(txt)
    

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}!')
#help(leiaInt)
