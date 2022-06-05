limpar = '\33[m'

cores = {
    'preto': '\33[30m',
    'vermelho': '\33[31m',
    'verde': '\33[32m',
    'amarelo': '\33[33m',
    'azul': '\33[34m',
    'roxo': '\33[35m',
    'ciano': '\33[36m',
    'cinza': '\33[37m',

    'cinza_escuro': '\33[90m',
    'vermelho_claro': '\33[91m',
    'verde_claro': '\33[92m',
    'amarelo_claro': '\33[93m',
    'azul_claro': '\33[94m',
    'roxo_claro': '\33[95m',
    'ciano_claro': '\33[96m',
    'branco': '\33[97m'
}

bg = {
    'branco': '\33[107m',
    'preto': '\33[40m',
    'vermelho': '\33[101m',
    'verde': '\33[102m',
    'amarelo': '\33[103m',
    'azul': '\33[104m',
    'roxo': '\33[105m',
    'ciano': '\33[106m',
}

fx = {


    'normal': '\33[10m',
    'contorno': '\33[52m',
    'negrito': '\33[1m',
    'italico': '\33[3m',
    'sublinhado': '\33[4m',
}

    
class Styles:

    def __init__(self):
        self.clear = '\33[m'
        self.black = '\33[30m'
        self.red = '\33[31m'
        self.green = '\33[32m'
        self.yellow = '\33[33m'
        self.blue = '\33[34m'
        self.purple = '\33[35m'
        self.cyan = '\33[36m'
        self.grey = '\33[37m'
        self.white = '\33[97m'
        self.darkgrey = '\33[90m'
        self.bred = '\33[91m'
        self.bgreen = '\33[92m'
        self.byellow = '\33[93m'
        self.bblue = '\33[94m'
        self.bpurple = '\33[95m'
        self.bcyan = '\33[96m'
        self.bg_white = '\33[107m'
        self.bg_black = '\33[40m'
        self.bg_red = '\33[101m'
        self.bg_green = '\33[102m'
        self.bg_yellow = '\33[103m'
        self.bg_blue = '\33[104m'
        self.bg_purple = '\33[105m'
        self.bg_cyan = '\33[106m'
        self.fx_plain = '\33[10m'
        self.fx_out = '\33[52m'
        self.fx_bold = '\33[1m'
        self.fx_italic = '\33[3m'
        self.fx_under = '\33[4m'