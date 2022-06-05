from cores import *
print('\033[0;97;41mOlá mundo lindo!\033[m')
print('\033[1;33;44mComo você tá? \033[m')
print('\033[1;35;43mEu estou testando cores no terminal \033[m')
print('\033[35;42mTá gostando? \033[m')
print('\033[mEsse aqui é pra ser padrão \033[m')
print('\033[0;30;107mE esse preto e branco usando a configuração atual \033[m')
#nao esquecer de colocar \033[m no final da frase dentro das aspas para indicar o final da formatação

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

print(f'{cores["roxo_claro"]}{bg["ciano"]}{fx["sublinhado"]}Esse é um exemplo de cor com fonte roxo claro, background ciano e sublinhado usando a biblioteca do meu namorado gênio! S2 {limpar}')