from cores import Styles
c = Styles()

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', c.white, c.bg_blue)
    print(c.black, c.bg_white)
    help(com)
    print(c.clear)


def titulo(msg, corLetra , corFundo):
    tam = len(msg) + 4
    print(f'{corLetra}{corFundo}~' * tam)
    print(f'  {msg}  ')
    print(f'~' * tam)
    print(c.clear)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', c.white, c.bg_purple)
    comando = input(f'Função ou Biblioteca >>>>>  ')
    if comando.upper() =='FIM':
        break
    else:
        ajuda(comando)
        
titulo(f'ATÉ LOGO!!', c.white, c.bg_red)
